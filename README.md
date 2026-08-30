# Python Customer Data Cleaner

A Python-based data cleaning tool that processes customer CSV files and automatically detects and fixes common data-quality issues.

## Features

- Reads customer data from CSV
- Detects duplicate records
- Removes duplicate records
- Detects missing values
- Fills missing ages using the average age
- Fills missing emails with "Not Provided"
- Exports cleaned CSV data
- Generates a data-cleaning summary report

## Technologies

- Python
- Pandas
- CSV
- Data Cleaning
- Data Processing

## Project Structure

Python-Data-Cleaner/
├── data/
├── output/
├── main.py
├── README.md
└── requirements.txt

## How to Run

Install dependencies:

    python -m pip install -r requirements.txt

Run the program:

    python main.py

## Example Results

Original records: 10

Duplicate records removed: 2

Final records: 8

Missing values are identified and cleaned automatically.

## Author

Leela Prasad Pottangi