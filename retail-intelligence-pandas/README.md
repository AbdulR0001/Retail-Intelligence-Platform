# Canadian Retail Intelligence Platform

A portfolio-ready Python and Pandas project that generates and analyzes a large synthetic retail dataset. The default configuration creates **250,000 transactions** plus controlled duplicate and missing-value issues for a realistic data-cleaning workflow.

## Business Questions

- What are total sales, profit, average order value, and return rate?
- Which categories, products, provinces, and channels perform best?
- How do sales change month by month?
- Which customer segments generate the most revenue?
- Where are returns concentrated?

## Main Skills Demonstrated

- Large CSV processing with Pandas
- Data cleaning and validation
- Missing-value and duplicate handling
- GroupBy, aggregation, sorting, and date features
- KPI and automated CSV report generation
- Matplotlib business charts
- Modular Python project structure
- Unit testing with pytest

## Project Structure

```text
retail-intelligence-pandas/
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── charts/
│   └── reports/
├── src/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── analyze_sales.py
│   ├── visualize.py
│   └── utils.py
├── tests/
│   └── test_clean_data.py
├── config.json
├── requirements.txt
├── run_project.py
└── README.md
```

## Quick Start

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Run the full project

```bash
python run_project.py
```

Generated data, reports, and charts will appear in the `data` and `outputs` folders.

### 4. Run tests

```bash
pytest
```

## Data Dictionary

The synthetic dataset includes order IDs, dates, customers, segments, provinces, sales channels, categories, products, quantity, pricing, costs, discounts, payment methods, delivery time, returns, and customer ratings.

## Important Note

The dataset is synthetic and generated locally. It does not contain real customer or company information.

## Suggested GitHub Description

Large-scale Canadian retail analytics project using Python and Pandas to clean and analyze 250,000 synthetic sales transactions, calculate business KPIs, generate automated reports, and visualize sales trends.
