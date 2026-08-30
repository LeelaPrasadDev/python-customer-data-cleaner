import pandas as pd

from main import clean_customer_data


def test_duplicate_records_are_removed(tmp_path):
    test_file = tmp_path / "customers.csv"

    data = pd.DataFrame({
        "Name": ["John", "John", "Alice"],
        "Age": [25, 25, 30],
        "Email": ["john@example.com", "john@example.com", "alice@example.com"]
    })

    data.to_csv(test_file, index=False)

    df, original_records, duplicates, missing_before = clean_customer_data(test_file)

    assert original_records == 3
    assert duplicates == 1
    assert len(df) == 2


def test_missing_values_are_cleaned(tmp_path):
    test_file = tmp_path / "customers.csv"

    data = pd.DataFrame({
        "Name": ["John", "Alice"],
        "Age": [25, None],
        "Email": ["john@example.com", None]
    })

    data.to_csv(test_file, index=False)

    df, original_records, duplicates, missing_before = clean_customer_data(test_file)

    assert df["Age"].isna().sum() == 0
    assert df["Email"].isna().sum() == 0
    assert "Not Provided" in df["Email"].values
