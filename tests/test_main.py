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
    def test_unique_records_are_preserved(tmp_path):
        test_file = tmp_path / "customers.csv"

        data = pd.DataFrame({
            "Name": ["John", "Alice", "Bob"],
            "Age": [25, 30, 35],
            "Email": [
                "john@example.com",
                "alice@example.com",
                "bob@example.com"
            ]
        })

        data.to_csv(test_file, index=False)

        df, original_records, duplicates, missing_before = clean_customer_data(test_file)

        assert original_records == 3
        assert duplicates == 0
        assert len(df) == 3

def test_duplicate_count_is_correct(tmp_path):
    test_file = tmp_path / "customers.csv"

    data = pd.DataFrame({
        "Name": ["John", "John", "John", "Alice"],
        "Age": [25, 25, 25, 30],
        "Email": [
            "john@example.com",
            "john@example.com",
            "john@example.com",
            "alice@example.com"
        ]
    })

    data.to_csv(test_file, index=False)

    df, original_records, duplicates, missing_before = clean_customer_data(test_file)

    assert original_records == 4
    assert duplicates == 2
    assert len(df) == 2

def test_cleaned_dataframe_has_expected_columns(tmp_path):
    test_file = tmp_path / "customers.csv"

    data = pd.DataFrame({
        "Name": ["John", "Alice"],
        "Age": [25, 30],
        "Email": [
            "john@example.com",
            "alice@example.com"
        ]
    })

    data.to_csv(test_file, index=False)

    df, original_records, duplicates, missing_before = clean_customer_data(test_file)

    assert "Name" in df.columns
    assert "Age" in df.columns
    assert "Email" in df.columns
