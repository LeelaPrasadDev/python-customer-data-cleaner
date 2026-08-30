# 🐍 Python Customer Data Cleaner

A Python and Pandas-based data cleaning tool that processes customer CSV files, detects common data-quality issues, removes duplicate records, handles missing values, and generates cleaned datasets and summary reports.

## 🎯 Project Overview

This project demonstrates a practical data-cleaning workflow using Python and Pandas.

It takes a raw customer CSV file containing duplicate records and missing values, cleans the dataset automatically, and produces a structured cleaned CSV file along with a summary report.

## ✨ Key Features

- 📂 Reads customer data from CSV files
- 🔍 Detects missing values
- 🧹 Removes duplicate records
- 📊 Fills missing age values using the average age
- 📧 Fills missing email addresses with `Not Provided`
- 💾 Generates a cleaned CSV dataset
- 📝 Generates an automatic cleaning summary report
- ⚡ Simple command-line execution

## 🛠️ Technologies

- Python 3
- Pandas
- CSV
- Data Cleaning
- Data Processing

## 📂 Project Structure

```text
Python-Data-Cleaner/
│
├── data/
│   └── customers.csv
│
├── output/
│   ├── cleaned_customers.csv
│   └── summary_report.txt
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
