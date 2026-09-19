import pandas as pd
from src.utils import ROOT, ensure_directories


def run_analysis():
    ensure_directories()
    source = ROOT / "data" / "processed" / "retail_sales_clean.csv"
    if not source.exists():
        raise FileNotFoundError("Run clean_data.py first.")
    df = pd.read_csv(source, parse_dates=["order_date"])
    reports = ROOT / "outputs" / "reports"

    kpis = pd.DataFrame({"metric": [
        "Orders", "Unique Customers", "Units Sold", "Net Sales",
        "Profit", "Average Order Value", "Return Rate (%)"
    ], "value": [
        df["order_id"].nunique(), df["customer_id"].nunique(), df["quantity"].sum(),
        round(df["net_sales"].sum(), 2), round(df["profit"].sum(), 2),
        round(df.groupby("order_id")["net_sales"].sum().mean(), 2),
        round(df["returned"].eq("Yes").mean() * 100, 2)
    ]})
    kpis.to_csv(reports / "executive_kpis.csv", index=False)

    aggregations = {
        "monthly_performance.csv": df.groupby("month", as_index=False).agg(orders=("order_id", "nunique"), units=("quantity", "sum"), sales=("net_sales", "sum"), profit=("profit", "sum")),
        "category_performance.csv": df.groupby("category", as_index=False).agg(orders=("order_id", "nunique"), units=("quantity", "sum"), sales=("net_sales", "sum"), profit=("profit", "sum"), avg_rating=("customer_rating", "mean")),
        "province_performance.csv": df.groupby("province", as_index=False).agg(orders=("order_id", "nunique"), sales=("net_sales", "sum"), profit=("profit", "sum")),
        "channel_performance.csv": df.groupby("sales_channel", as_index=False).agg(orders=("order_id", "nunique"), sales=("net_sales", "sum"), profit=("profit", "sum")),
        "top_products.csv": df.groupby(["category", "product"], as_index=False).agg(units=("quantity", "sum"), sales=("net_sales", "sum"), profit=("profit", "sum")).sort_values("sales", ascending=False),
        "customer_segments.csv": df.groupby("customer_segment", as_index=False).agg(customers=("customer_id", "nunique"), orders=("order_id", "nunique"), sales=("net_sales", "sum"), profit=("profit", "sum")),
        "return_analysis.csv": df.groupby(["category", "returned"], as_index=False).agg(orders=("order_id", "nunique"), sales=("net_sales", "sum")),
    }
    for filename, report in aggregations.items():
        numeric = report.select_dtypes("number").columns
        report[numeric] = report[numeric].round(2)
        report.to_csv(reports / filename, index=False)

    print(f"Created {1 + len(aggregations)} reports in {reports}")
    return kpis


if __name__ == "__main__":
    run_analysis()
