import json
import random

random.seed(42)

categories = {
    "Smartphones": {
        "brands": ["Samsung", "Apple", "OnePlus", "Xiaomi", "Realme", "Vivo", "Oppo", "Google", "Motorola", "Nokia"],
        "models": ["Pro Max", "Ultra", "Plus", "Lite", "Neo", "Edge", "Fusion", "Series", "X", "S"],
        "price_range": (8999, 149999),
        "emoji": "📱"
    },
    "Laptops": {
        "brands": ["Dell", "HP", "Lenovo", "Asus", "Acer", "Apple", "MSI", "Razer", "LG", "Microsoft"],
        "models": ["Inspiron", "Pavilion", "ThinkPad", "VivoBook", "Aspire", "MacBook", "Prestige", "Blade", "Gram", "Surface"],
        "price_range": (25999, 249999),
        "emoji": "💻"
    },
    "Headphones": {
        "brands": ["Sony", "Bose", "JBL", "Sennheiser", "Audio-Technica", "Boat", "Jabra", "Skullcandy", "AKG", "Beyerdynamic"],
        "models": ["WH-1000XM", "QuietComfort", "Tune", "Momentum", "ATH-M", "Rockerz", "Evolve", "Crusher", "K", "DT"],
        "price_range": (799, 49999),
        "emoji": "🎧"
    },
    "Tablets": {
        "brands": ["Apple", "Samsung", "Lenovo", "Xiaomi", "Realme", "Amazon", "Microsoft", "Huawei", "OnePlus", "TCL"],
        "models": ["iPad Pro", "Galaxy Tab", "Tab P", "Pad", "Pad X", "Fire", "Surface Go", "MatePad", "Pad Air", "Tab"],
        "price_range": (9999, 119999),
        "emoji": "📟"
    },
    "Smart Watches": {
        "brands": ["Apple", "Samsung", "Garmin", "Fitbit", "Amazfit", "Boat", "Noise", "Fossil", "Huawei", "Realme"],
        "models": ["Watch Ultra", "Galaxy Watch", "Fenix", "Sense", "GTR", "Storm", "ColorFit", "Gen", "Watch GT", "Watch S"],
        "price_range": (1299, 79999),
        "emoji": "⌚"
    },
    "Cameras": {
        "brands": ["Canon", "Nikon", "Sony", "Fujifilm", "Panasonic", "Olympus", "GoPro", "DJI", "Leica", "Pentax"],
        "models": ["EOS", "D-Series", "Alpha", "X-Series", "Lumix", "OM-D", "Hero", "Osmo", "Q", "K"],
        "price_range": (14999, 349999),
        "emoji": "📷"
    },
    "Televisions": {
        "brands": ["Samsung", "LG", "Sony", "TCL", "Hisense", "Xiaomi", "OnePlus", "Vu", "Toshiba", "Philips"],
        "models": ["QLED", "OLED", "Bravia", "4K UHD", "U8", "TV Pro", "Smart TV", "Iconium", "Regza", "Ambilight"],
        "price_range": (12999, 499999),
        "emoji": "📺"
    },
    "Gaming": {
        "brands": ["PlayStation", "Xbox", "Nintendo", "Razer", "Logitech", "SteelSeries", "Corsair", "HyperX", "ASUS ROG", "MSI"],
        "models": ["DualSense", "Elite", "Pro Controller", "Huntsman", "G Pro", "Apex", "K70", "Cloud", "Gladius", "Clutch"],
        "price_range": (1999, 89999),
        "emoji": "🎮"
    },
    "Speakers": {
        "brands": ["JBL", "Bose", "Sony", "Marshall", "Ultimate Ears", "Boat", "Harman", "Anker", "Zebronics", "Philips"],
        "models": ["Flip", "SoundLink", "XB", "Acton", "Boom", "Stone", "Onyx", "Soundcore", "Zeb", "TAS"],
        "price_range": (999, 59999),
        "emoji": "🔊"
    },
    "Accessories": {
        "brands": ["Anker", "Belkin", "Ugreen", "Boat", "Zebronics", "TP-Link", "D-Link", "portronics", "Syska", "AmazonBasics"],
        "models": ["PowerCore", "Boost", "Nexode", "Deuce", "Zeb-Switch", "Archer", "DIR", "Mport", "LED", "USB Hub"],
        "price_range": (299, 9999),
        "emoji": "🔌"
    }
}

ratings_pool = [3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0]
specs_pool = {
    "Smartphones": ["6.7-inch AMOLED", "5000mAh Battery", "108MP Camera", "5G Ready", "256GB Storage", "12GB RAM", "Fast Charging 67W", "IP68 Water Resistant"],
    "Laptops": ["Intel Core i7", "16GB DDR5 RAM", "512GB NVMe SSD", "15.6-inch FHD IPS", "NVIDIA RTX 4060", "Backlit Keyboard", "Wi-Fi 6E", "Thunderbolt 4"],
    "Headphones": ["Active Noise Cancellation", "30hr Battery Life", "Hi-Res Audio", "Bluetooth 5.3", "Foldable Design", "40mm Drivers", "Multipoint Connection", "IPX4 Rating"],
    "Tablets": ["10.9-inch Liquid Retina", "M2 Chip", "256GB Storage", "Wi-Fi 6", "5G Option", "12MP Camera", "USB-C", "All-Day Battery"],
    "Smart Watches": ["AMOLED Display", "GPS Built-in", "Heart Rate Monitor", "Blood Oxygen Sensor", "7-day Battery", "100+ Sport Modes", "Water Resistant 5ATM", "Sleep Tracking"],
    "Cameras": ["24.1MP APS-C Sensor", "4K Video", "Dual Pixel AF", "5-Axis Stabilization", "Weather Sealed", "Wi-Fi + Bluetooth", "Flip Screen", "RAW Support"],
    "Televisions": ["4K UHD Resolution", "HDR10+", "Dolby Atmos", "120Hz Refresh Rate", "HDMI 2.1", "Smart TV Android", "Voice Control", "Gaming Mode"],
    "Gaming": ["Mechanical Switches", "RGB Lighting", "8K DPI Sensor", "Wireless 2.4GHz", "Anti-ghosting", "Programmable Buttons", "Ergonomic Design", "USB-C Charging"],
    "Speakers": ["360° Sound", "Waterproof IPX7", "20hr Playtime", "Dual Passive Radiators", "Bluetooth 5.3", "USB-C Charging", "Party Boost", "App Control"],
    "Accessories": ["GaN Technology", "65W Fast Charging", "4-Port USB Hub", "Braided Cable", "Universal Compatibility", "Surge Protection", "Compact Design", "Multi-device"]
}

colors_pool = ["Midnight Black", "Pearl White", "Cosmic Blue", "Forest Green", "Rose Gold", "Titanium Gray", "Phantom Violet", "Ice Silver"]

products = []
pid = 1

for category, data in categories.items():
    target = 105  # ~105 per category = ~1050 total
    brands = data["brands"]
    models = data["models"]
    min_p, max_p = data["price_range"]
    specs = specs_pool[category]

    for i in range(target):
        brand = brands[i % len(brands)]
        model = models[i % len(models)]
        variant = random.randint(1, 9)
        name = f"{brand} {model} {variant}"

        price = random.randint(min_p // 100, max_p // 100) * 100
        discount = random.choice([0, 5, 10, 15, 20, 25, 30])
        original_price = int(price / (1 - discount / 100)) if discount > 0 else price
        rating = random.choice(ratings_pool)
        reviews = random.randint(12, 8500)
        stock = random.randint(0, 200)
        color = random.choice(colors_pool)
        prod_specs = random.sample(specs, min(4, len(specs)))
        is_new = random.random() < 0.15
        is_featured = random.random() < 0.1

        products.append({
            "id": pid,
            "name": name,
            "brand": brand,
            "category": category,
            "price": price,
            "original_price": original_price,
            "discount": discount,
            "rating": rating,
            "reviews": reviews,
            "stock": stock,
            "color": color,
            "specs": prod_specs,
            "is_new": is_new,
            "is_featured": is_featured,
            "emoji": data["emoji"],
            "image_seed": pid  # used for placeholder image
        })
        pid += 1

with open("/home/claude/techmart/data/products.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"Generated {len(products)} products across {len(categories)} categories")
for cat in categories:
    count = sum(1 for p in products if p["category"] == cat)
    print(f"  {cat}: {count}")
