import matplotlib.pyplot as plt
import pandas as pd
from src.utils import ROOT, ensure_directories


def save_bar(data, x, y, title, filename, rotation=0):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x], data[y])
    plt.title(title)
    plt.xlabel(x.replace("_", " ").title())
    plt.ylabel(y.replace("_", " ").title())
    plt.xticks(rotation=rotation, ha="right" if rotation else "center")
    plt.tight_layout()
    plt.savefig(ROOT / "outputs" / "charts" / filename, dpi=150)
    plt.close()


def create_charts():
    ensure_directories()
    reports = ROOT / "outputs" / "reports"
    monthly = pd.read_csv(reports / "monthly_performance.csv")
    category = pd.read_csv(reports / "category_performance.csv")
    province = pd.read_csv(reports / "province_performance.csv")
    products = pd.read_csv(reports / "top_products.csv").head(10)

    plt.figure(figsize=(12, 6))
    plt.plot(monthly["month"], monthly["sales"], marker="o", linewidth=2)
    plt.title("Monthly Net Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Net Sales")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(ROOT / "outputs" / "charts" / "monthly_sales_trend.png", dpi=150)
    plt.close()

    save_bar(category.sort_values("sales", ascending=False), "category", "sales", "Sales by Category", "sales_by_category.png")
    save_bar(province.sort_values("profit", ascending=False), "province", "profit", "Profit by Province", "profit_by_province.png")
    save_bar(products.sort_values("sales"), "product", "sales", "Top 10 Products by Sales", "top_products.png", 45)
    print(f"Created 4 charts in {ROOT / 'outputs' / 'charts'}")


if __name__ == "__main__":
    create_charts()
