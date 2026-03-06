from fastapi import FastAPI

app = FastAPI()

# Product list
products = [
    {"id": 1, "name": "Smartphone", "price": 699, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Headphones", "price": 199, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Notebook", "price": 5, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Pen", "price": 2, "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 39, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 129, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 79, "category": "Electronics", "in_stock": False}
]

# Get all products
@app.get("/products")
def get_products():
    return {
        "total_products": len(products),
        "items": products
    }

# Filter products by category
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    filtered_products = [
        p for p in products if p["category"].lower() == category_name.lower()
    ]

    if not filtered_products:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "items": filtered_products
    }

# Show only in-stock products
@app.get("/products/instock")
def get_instock_products():
    in_stock_products = [p for p in products if p["in_stock"]]

    return {
        "in_stock_products": in_stock_products,
        "count": len(in_stock_products)
    }

# Store info Endpoint
@app.get("/store/summary")
def store_summary():
    total_products = len(products)
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_of_stock_count = total_products - in_stock_count

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }

# Search Products by Name
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    matched_products = [
        p for p in products if keyword.lower() in p["name"].lower()
    ]

    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "matches": matched_products,
        "count": len(matched_products)
    }

# Cheapest & Most Expensive Product
@app.get("/products/deals")
def get_product_deals():
    best_deal = min(products, key=lambda p: p["price"])
    premium_pick = max(products, key=lambda p: p["price"])

    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }