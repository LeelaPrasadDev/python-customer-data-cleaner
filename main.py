import argparse
import pandas as pd


INPUT_FILE = "data/customers.csv"
OUTPUT_FILE = "output/cleaned_customers.csv"
REPORT_FILE = "output/summary_report.txt"


def clean_customer_data(input_file=INPUT_FILE):
    """Load and clean customer data."""

    df = pd.read_csv(input_file)

    original_records = len(df)

    # Count missing values before cleaning
    missing_before = df.isnull().sum()

    # Count duplicate records
    duplicates = df.duplicated().sum()

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing age values with average age
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].mean())

    # Fill missing email addresses
    if "Email" in df.columns:
        df["Email"] = df["Email"].fillna("Not Provided")

    return df, original_records, duplicates, missing_before


def save_cleaned_data(df, output_file=OUTPUT_FILE):
    """Save the cleaned customer data."""

    df.to_csv(output_file, index=False)


def generate_report(
    original_records,
    duplicates,
    final_records,
    missing_before,
    report_file=REPORT_FILE,
):
    """Generate a summary report."""

    with open(report_file, "w") as report:
        report.write("=== CUSTOMER DATA CLEANING REPORT ===\n\n")
        report.write(f"Original records: {original_records}\n")
        report.write(f"Duplicate records removed: {duplicates}\n")
        report.write(f"Final records: {final_records}\n\n")

        report.write("Missing values before cleaning:\n")

        for column, count in missing_before.items():
            report.write(f"{column}: {count}\n")

        report.write("\nCleaning completed successfully.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Clean customer CSV data and generate a summary report."
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        default=INPUT_FILE,
        help="Path to the input customer CSV file."
    )

    parser.add_argument(
        "--output",
        default=OUTPUT_FILE,
        help="Path for the cleaned CSV file."
    )

    parser.add_argument(
        "--report",
        default=REPORT_FILE,
        help="Path for the summary report."
    )

    args = parser.parse_args()

    print("=== CUSTOMER DATA CLEANER ===")

    df, original_records, duplicates, missing_before = clean_customer_data(
        args.input_file
    )

    save_cleaned_data(df, args.output)

    generate_report(
        original_records,
        duplicates,
        len(df),
        missing_before,
        args.report
    )

    print(f"Original records: {original_records}")
    print(f"Duplicates removed: {duplicates}")
    print(f"Final records: {len(df)}")
    print(f"Cleaned file: {args.output}")
    print(f"Report file: {args.report}")
    print("Data cleaning completed successfully!")


if __name__ == "__main__":
    main()
