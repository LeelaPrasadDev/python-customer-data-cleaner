# 🐍 Python Customer Data Cleaner

A Python and Pandas-based data cleaning tool that processes customer CSV files, detects common data-quality issues, removes duplicate records, handles missing values, and generates cleaned datasets and summary reports.

## 🎯 Project Overview

This project demonstrates a practical data-cleaning workflow using **Python** and **Pandas**.

The tool takes a raw customer CSV file containing duplicate records and missing values, cleans the dataset automatically, and generates a structured cleaned CSV file along with a summary report.

## ✨ Key Features

- 📂 Reads customer data from CSV files
- 🔍 Detects missing values
- 🗑️ Removes duplicate customer records
- 📊 Fills missing age values using the average age
- 📧 Fills missing email addresses with `Not Provided`
- 🧹 Generates a cleaned customer dataset
- 📄 Generates an automatic cleaning summary report
- ⚡ Simple command-line execution

## 🛠️ Technologies Used

- 🐍 Python 3
- 🐼 Pandas
- 📄 CSV
- 🔧 Data Cleaning
- 📊 Data Processing

## 📁 Project Structure

```text
python-customer-data-cleaner/
│
├── data/
│   └── customers.csv
│
├── output/
│   ├── cleaned_customers.csv
│   └── summary_report.txt
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
