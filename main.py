import pandas as pd

# File paths
input_file = "data/customers.csv"
output_file = "output/cleaned_customers.csv"
report_file = "output/summary_report.txt"

# Read the CSV file
df = pd.read_csv(input_file)

print("=== CUSTOMER DATA CLEANER ===")
print(f"Original records: {len(df)}")

# Check missing values
missing_before = df.isnull().sum()

# Check duplicate records
duplicates = df.duplicated().sum()

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Email with "Not Provided"
df["Email"] = df["Email"].fillna("Not Provided")

# Save cleaned data
df.to_csv(output_file, index=False)

# Create summary report
with open(report_file, "w") as report:
    report.write("CUSTOMER DATA CLEANING REPORT\n")
    report.write("=" * 35 + "\n\n")
    report.write(f"Original records: {len(pd.read_csv(input_file))}\n")
    report.write(f"Duplicate records removed: {duplicates}\n")
    report.write(f"Final records: {len(df)}\n\n")

    report.write("Missing values before cleaning:\n")
    for column, count in missing_before.items():
        report.write(f"- {column}: {count}\n")

    report.write("\nCleaning completed successfully.\n")

print(f"Duplicates removed: {duplicates}")
print(f"Final records: {len(df)}")
print(f"Cleaned file: {output_file}")
print(f"Report file: {report_file}")
print("\nData cleaning completed successfully!")