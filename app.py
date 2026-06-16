from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import json
import math

app = Flask(__name__)
app.secret_key = "techmart_secret_key_2025"

# ── Load products ──────────────────────────────────────────
with open("data/products.json") as f:
    ALL_PRODUCTS = json.load(f)

CATEGORIES = sorted(set(p["category"] for p in ALL_PRODUCTS))
BRANDS     = sorted(set(p["brand"]    for p in ALL_PRODUCTS))
PER_PAGE   = 24


def get_cart():
    return session.get("cart", {})


def cart_total(cart):
    total = 0
    for pid, item in cart.items():
        total += item["price"] * item["qty"]
    return total


def cart_count(cart):
    return sum(item["qty"] for item in cart.values())


# ── Routes ──────────────────────────────────────────────────

@app.route("/")
def index():
    featured   = [p for p in ALL_PRODUCTS if p["is_featured"]][:8]
    new_arrive = [p for p in ALL_PRODUCTS if p["is_new"]][:8]
    top_rated  = sorted(ALL_PRODUCTS, key=lambda p: p["rating"], reverse=True)[:8]
    deals      = sorted(ALL_PRODUCTS, key=lambda p: p["discount"], reverse=True)[:8]
    cart = get_cart()
    return render_template("index.html",
        featured=featured,
        new_arrivals=new_arrive,
        top_rated=top_rated,
        deals=deals,
        categories=CATEGORIES,
        cart_count=cart_count(cart)
    )


@app.route("/products")
def products():
    q          = request.args.get("q", "").strip().lower()
    category   = request.args.get("category", "")
    brand      = request.args.get("brand", "")
    min_price  = request.args.get("min_price", type=int, default=0)
    max_price  = request.args.get("max_price", type=int, default=500000)
    min_rating = request.args.get("min_rating", type=float, default=0)
    sort_by    = request.args.get("sort", "popular")
    page       = request.args.get("page", type=int, default=1)
    in_stock   = request.args.get("in_stock", "")

    results = ALL_PRODUCTS[:]

    if q:
        results = [p for p in results if q in p["name"].lower() or q in p["brand"].lower() or q in p["category"].lower()]
    if category:
        results = [p for p in results if p["category"] == category]
    if brand:
        results = [p for p in results if p["brand"] == brand]
    if min_price:
        results = [p for p in results if p["price"] >= min_price]
    if max_price < 500000:
        results = [p for p in results if p["price"] <= max_price]
    if min_rating:
        results = [p for p in results if p["rating"] >= min_rating]
    if in_stock:
        results = [p for p in results if p["stock"] > 0]

    sort_map = {
        "popular":    lambda p: p["reviews"],
        "rating":     lambda p: p["rating"],
        "price_asc":  lambda p: p["price"],
        "price_desc": lambda p: -p["price"],
        "discount":   lambda p: p["discount"],
        "newest":     lambda p: p["is_new"],
    }
    results = sorted(results, key=sort_map.get(sort_by, sort_map["popular"]), reverse=True)

    total    = len(results)
    pages    = math.ceil(total / PER_PAGE)
    start    = (page - 1) * PER_PAGE
    products_page = results[start:start + PER_PAGE]

    cart = get_cart()
    return render_template("products.html",
        products=products_page,
        categories=CATEGORIES,
        brands=BRANDS,
        total=total,
        page=page,
        pages=pages,
        query=q,
        selected_category=category,
        selected_brand=brand,
        min_price=min_price,
        max_price=max_price,
        min_rating=min_rating,
        sort_by=sort_by,
        in_stock=in_stock,
        cart_count=cart_count(cart)
    )


@app.route("/product/<int:pid>")
def product_detail(pid):
    product = next((p for p in ALL_PRODUCTS if p["id"] == pid), None)
    if not product:
        return "Product not found", 404

    related = [p for p in ALL_PRODUCTS
               if p["category"] == product["category"] and p["id"] != pid][:6]

    cart = get_cart()
    in_cart = str(pid) in cart
    return render_template("product_detail.html",
        product=product,
        related=related,
        categories=CATEGORIES,
        in_cart=in_cart,
        cart_count=cart_count(cart)
    )


@app.route("/cart")
def cart():
    cart = get_cart()
    items = []
    for pid, item in cart.items():
        product = next((p for p in ALL_PRODUCTS if p["id"] == int(pid)), None)
        if product:
            items.append({**product, "qty": item["qty"]})
    total  = cart_total(cart)
    count  = cart_count(cart)
    return render_template("cart.html",
        items=items,
        total=total,
        categories=CATEGORIES,
        cart_count=count
    )


@app.route("/cart/add/<int:pid>", methods=["POST"])
def add_to_cart(pid):
    product = next((p for p in ALL_PRODUCTS if p["id"] == pid), None)
    if not product:
        return jsonify({"error": "Not found"}), 404

    cart = get_cart()
    key = str(pid)
    if key in cart:
        cart[key]["qty"] += 1
    else:
        cart[key] = {"name": product["name"], "price": product["price"], "qty": 1}
    session["cart"] = cart

    return jsonify({"success": True, "cart_count": cart_count(cart), "message": f"'{product['name']}' added to cart!"})


@app.route("/cart/remove/<int:pid>", methods=["POST"])
def remove_from_cart(pid):
    cart = get_cart()
    cart.pop(str(pid), None)
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/cart/update/<int:pid>", methods=["POST"])
def update_cart(pid):
    qty = int(request.form.get("qty", 1))
    cart = get_cart()
    key = str(pid)
    if key in cart:
        if qty <= 0:
            cart.pop(key)
        else:
            cart[key]["qty"] = qty
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/checkout")
def checkout():
    cart = get_cart()
    items = []
    for pid, item in cart.items():
        product = next((p for p in ALL_PRODUCTS if p["id"] == int(pid)), None)
        if product:
            items.append({**product, "qty": item["qty"]})
    total = cart_total(cart)
    return render_template("checkout.html",
        items=items,
        total=total,
        categories=CATEGORIES,
        cart_count=cart_count(cart)
    )


@app.route("/checkout/place", methods=["POST"])
def place_order():
    session["cart"] = {}
    return render_template("order_success.html", categories=CATEGORIES, cart_count=0)


@app.route("/category/<cat>")
def category(cat):
    return redirect(url_for("products", category=cat))


@app.route("/api/search")
def api_search():
    q = request.args.get("q", "").strip().lower()
    if len(q) < 2:
        return jsonify([])
    results = [p for p in ALL_PRODUCTS if q in p["name"].lower() or q in p["brand"].lower()][:8]
    return jsonify([{"id": p["id"], "name": p["name"], "price": p["price"], "category": p["category"]} for p in results])


if __name__ == "__main__":
    app.run(debug=True)
