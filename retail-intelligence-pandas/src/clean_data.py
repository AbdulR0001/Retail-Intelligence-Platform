import pandas as pd
from src.utils import ROOT, ensure_directories

REQUIRED_COLUMNS = [
    "order_id", "order_date", "customer_id", "province", "category",
    "product", "quantity", "unit_price", "unit_cost", "discount_pct"
]


def clean_dataframe(df):
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    clean = df.copy()
    clean.columns = clean.columns.str.strip().str.lower()
    clean["order_date"] = pd.to_datetime(clean["order_date"], errors="coerce")
    clean = clean.drop_duplicates(subset="order_id", keep="first")
    clean = clean.dropna(subset=["order_id", "order_date", "unit_price", "quantity"])
    clean["customer_rating"] = clean.groupby("category")["customer_rating"].transform(lambda x: x.fillna(x.median()))
    clean["quantity"] = pd.to_numeric(clean["quantity"], errors="coerce").fillna(0).astype(int)
    clean["gross_sales"] = clean["quantity"] * clean["unit_price"]
    clean["discount_amount"] = clean["gross_sales"] * clean["discount_pct"]
    clean["net_sales"] = clean["gross_sales"] - clean["discount_amount"]
    clean["cost"] = clean["quantity"] * clean["unit_cost"]
    clean["profit"] = clean["net_sales"] - clean["cost"]
    clean["profit_margin_pct"] = (clean["profit"] / clean["net_sales"].replace(0, pd.NA) * 100).fillna(0)
    clean["year"] = clean["order_date"].dt.year
    clean["month"] = clean["order_date"].dt.to_period("M").astype(str)
    clean["quarter"] = clean["order_date"].dt.to_period("Q").astype(str)
    return clean


def clean_dataset():
    ensure_directories()
    source = ROOT / "data" / "raw" / "retail_sales.csv"
    if not source.exists():
        raise FileNotFoundError("Run generate_data.py first.")
    raw = pd.read_csv(source)
    clean = clean_dataframe(raw)
    output = ROOT / "data" / "processed" / "retail_sales_clean.csv"
    clean.to_csv(output, index=False)
    print(f"Saved {len(clean):,} clean rows at {output}")
    return clean


if __name__ == "__main__":
    clean_dataset()
