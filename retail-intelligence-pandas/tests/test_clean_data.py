import pandas as pd
from src.clean_data import clean_dataframe


def test_clean_dataframe_removes_duplicate_orders_and_creates_metrics():
    sample = pd.DataFrame({
        "order_id": ["A1", "A1", "A2"],
        "order_date": ["2025-01-01", "2025-01-01", "2025-02-01"],
        "customer_id": ["C1", "C1", "C2"],
        "province": ["BC", "BC", "ON"],
        "category": ["Books", "Books", "Home"],
        "product": ["Novel", "Novel", "Desk"],
        "quantity": [2, 2, 1],
        "unit_price": [20.0, 20.0, 100.0],
        "unit_cost": [8.0, 8.0, 50.0],
        "discount_pct": [0.1, 0.1, 0.0],
        "customer_rating": [5, 5, None],
        "returned": ["No", "No", "Yes"],
    })
    clean = clean_dataframe(sample)
    assert len(clean) == 2
    assert {"net_sales", "profit", "month", "quarter"}.issubset(clean.columns)
    assert clean.loc[clean["order_id"] == "A1", "net_sales"].iloc[0] == 36.0
