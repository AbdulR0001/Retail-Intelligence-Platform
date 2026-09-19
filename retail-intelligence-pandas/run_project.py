from src.generate_data import generate_dataset
from src.clean_data import clean_dataset
from src.analyze_sales import run_analysis
from src.visualize import create_charts


def main():
    print("1/4 Generating large retail dataset...")
    generate_dataset()
    print("2/4 Cleaning and validating data...")
    clean_dataset()
    print("3/4 Creating business reports...")
    run_analysis()
    print("4/4 Creating charts...")
    create_charts()
    print("Done. Open outputs/reports and outputs/charts.")


if __name__ == "__main__":
    main()
