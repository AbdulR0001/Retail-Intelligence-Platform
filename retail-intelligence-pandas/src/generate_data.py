import numpy as np
import pandas as pd
from src.utils import ROOT, ensure_directories, load_config

PRODUCTS = {
    "Electronics": (["Laptop", "Monitor", "Keyboard", "Headphones"], (45, 1800)),
    "Home": (["Desk", "Chair", "Lamp", "Coffee Maker"], (15, 750)),
    "Sports": (["Bicycle", "Yoga Mat", "Dumbbells", "Running Shoes"], (20, 1200)),
    "Clothing": (["Jacket", "Jeans", "Shirt", "Sneakers"], (18, 350)),
    "Books": (["Technology Book", "Business Book", "Novel", "Cookbook"], (10, 80)),
}


def generate_dataset(rows=None):
    config = load_config()
    rows = rows or config["rows"]
    rng = np.random.default_rng(config["random_seed"])
    ensure_directories()

    categories = np.array(list(PRODUCTS))
    category = rng.choice(categories, rows, p=[0.28, 0.20, 0.18, 0.22, 0.12])
    product = []
    unit_price = np.empty(rows)
    for i, cat in enumerate(category):
        names, price_range = PRODUCTS[cat]
        product.append(rng.choice(names))
        unit_price[i] = round(rng.uniform(*price_range), 2)

    dates = pd.to_datetime(rng.integers(
        pd.Timestamp(config["start_date"]).value // 10**9,
        pd.Timestamp(config["end_date"]).value // 10**9,
        rows,
    ), unit="s")
    quantity = rng.integers(1, 8, rows)
    discount = rng.choice([0, 0.05, 0.10, 0.15, 0.20], rows, p=[0.42, 0.18, 0.20, 0.12, 0.08])
    unit_cost = np.round(unit_price * rng.uniform(0.48, 0.76, rows), 2)
    returned = rng.choice(["No", "Yes"], rows, p=[0.93, 0.07])

    df = pd.DataFrame({
        "order_id": [f"ORD-{i:07d}" for i in range(1, rows + 1)],
        "order_date": dates,
        "customer_id": [f"CUS-{x:06d}" for x in rng.integers(1, 65001, rows)],
        "customer_age": rng.integers(18, 76, rows),
        "customer_segment": rng.choice(["Consumer", "Corporate", "Small Business"], rows, p=[0.58, 0.24, 0.18]),
        "province": rng.choice(["BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS"], rows, p=[0.16, 0.13, 0.05, 0.05, 0.35, 0.18, 0.035, 0.045]),
        "sales_channel": rng.choice(["Online", "Retail Store", "Marketplace"], rows, p=[0.50, 0.36, 0.14]),
        "category": category,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "unit_cost": unit_cost,
        "discount_pct": discount,
        "payment_method": rng.choice(["Credit Card", "Debit Card", "PayPal", "Gift Card"], rows, p=[0.46, 0.28, 0.20, 0.06]),
        "shipping_days": rng.integers(1, 11, rows),
        "returned": returned,
        "customer_rating": rng.choice([1, 2, 3, 4, 5], rows, p=[0.04, 0.08, 0.18, 0.36, 0.34]),
    })

    # Add controlled quality issues for a realistic cleaning workflow.
    missing_idx = rng.choice(df.index, max(1, rows // 200), replace=False)
    df.loc[missing_idx, "customer_rating"] = np.nan
    duplicates = df.sample(max(1, rows // 1000), random_state=config["random_seed"])
    df = pd.concat([df, duplicates], ignore_index=True)
    output = ROOT / "data" / "raw" / "retail_sales.csv"
    df.to_csv(output, index=False)
    print(f"Created {len(df):,} raw rows at {output}")
    return df


if __name__ == "__main__":
    generate_dataset()
