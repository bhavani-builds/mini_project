<div align="center">

# ⚡ TechMart

### Full-Stack E-Commerce Store for Electronics & Gadgets

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A complete e-commerce web app with 1050+ products, cart, search, filters, and checkout — built with Python Flask.**

</div>

---

## 🖥️ Live Preview

> Run locally in 3 commands — see below.

**Pages included:**
- 🏠 Homepage with Featured, Deals, New Arrivals, Top Rated sections
- 📦 Products listing with filters, sorting, and pagination
- 🔍 Live search with instant dropdown results
- 📄 Product detail page with specs and related products
- 🛒 Shopping cart with quantity controls
- 💳 Checkout page with multiple payment options
- ✅ Order success confirmation

---

## ✨ Features

- **1050+ Products** across 10 categories (Smartphones, Laptops, Headphones, Tablets, Smart Watches, Cameras, TVs, Gaming, Speakers, Accessories)
- **Advanced Filtering** — by category, brand, price range, rating, stock
- **Sorting** — by popularity, rating, price, discount, newest
- **Live Search** — instant results as you type
- **Shopping Cart** — add, update quantity, remove items (session-based)
- **Checkout Flow** — shipping address + payment options
- **Responsive Design** — works on mobile, tablet, desktop
- **Professional UI** — dark navbar, category pills, product cards with badges
- **Pagination** — 24 products per page with smart page navigation

---

## 🗂️ Project Structure

```
techmart/
├── app.py                  # Flask routes & logic
├── requirements.txt
├── generate_products.py    # Script to regenerate product data
├── data/
│   └── products.json       # 1050 product entries
├── templates/
│   ├── base.html           # Navbar, footer, layout
│   ├── index.html          # Homepage
│   ├── products.html       # Product listing + filters
│   ├── product_detail.html # Single product page
│   ├── cart.html           # Shopping cart
│   ├── checkout.html       # Checkout form
│   ├── order_success.html  # Order confirmation
│   └── partials/
│       └── product_card.html
├── static/
│   ├── css/style.css       # Complete stylesheet
│   └── js/main.js          # Cart AJAX, live search, UI
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/techmart.git
cd techmart
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5000
```

That's it! No database setup, no environment variables needed.

---

## 🛍️ Categories & Products

| Category | Products | Price Range |
|----------|----------|-------------|
| 📱 Smartphones | 105 | ₹8,999 – ₹1,49,999 |
| 💻 Laptops | 105 | ₹25,999 – ₹2,49,999 |
| 🎧 Headphones | 105 | ₹799 – ₹49,999 |
| 📟 Tablets | 105 | ₹9,999 – ₹1,19,999 |
| ⌚ Smart Watches | 105 | ₹1,299 – ₹79,999 |
| 📷 Cameras | 105 | ₹14,999 – ₹3,49,999 |
| 📺 Televisions | 105 | ₹12,999 – ₹4,99,999 |
| 🎮 Gaming | 105 | ₹1,999 – ₹89,999 |
| 🔊 Speakers | 105 | ₹999 – ₹59,999 |
| 🔌 Accessories | 105 | ₹299 – ₹9,999 |

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.8+, Flask 3.0 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Data | JSON (1050 products) |
| Session | Flask session (server-side) |
| Fonts | Google Fonts (Inter, Space Grotesk) |

No database required — all data is loaded from `products.json` into memory.

---

## 📸 Screenshots

> Add screenshots of your running app here!

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your branch (`git checkout -b feature/amazing-feature`)
3. Commit (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT © [bhavani](https://github.com/bhavani_builds)

---

<div align="center">
If you found this useful, give it a ⭐ on GitHub!
</div>
