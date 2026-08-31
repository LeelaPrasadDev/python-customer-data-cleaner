# 🐍 Python Customer Data Cleaner

A Python and Pandas-based data-cleaning tool that processes customer CSV files, detects common data-quality issues, removes duplicate records, handles missing values, and generates cleaned datasets with summary reports.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![Tests](https://github.com/LeelaPrasadDev/python-customer-data-cleaner/actions/workflows/tests.yml/badge.svg)

---

## 🎯 Project Overview

This project demonstrates a practical data-cleaning workflow using **Python** and **Pandas**.

The tool takes a raw customer CSV file containing duplicate records and missing values, cleans the dataset automatically, and generates:

- A cleaned customer CSV file
- A data-cleaning summary report

---

## ✨ Key Features

- 📂 Reads customer data from CSV files
- 🔍 Detects missing values
- 🧹 Removes duplicate customer records
- 📊 Fills missing age values using the average age
- 📧 Fills missing email addresses with `Not Provided`
- 💾 Generates a cleaned CSV dataset
- 📝 Generates an automatic cleaning summary report
- ⚡ Simple command-line execution
- 🤖 Automated testing with GitHub Actions

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- CSV
- Pytest
- GitHub Actions
- Data Cleaning
- Data Processing

---

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/LeelaPrasadDev/python-customer-data-cleaner.git
cd python-customer-data-cleaner
```
---

## 📁 Project Structure

```text
python-customer-data-cleaner/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── data/
│   └── customers.csv
│
├── output/
│   ├── cleaned_customers.csv
│   └── summary_report.txt
│
├── tests/
│   └── test_main.py
│
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── requirements.txt
```

## 📊 Results

The data-cleaning process produced the following results:

| Metric | Result |
|---|---:|
| Original records | 10 |
| Duplicate records removed | 2 |
| Final records | 8 |
| Missing Age | Filled with average age |
| Missing Email | Filled with `Not Provided` |
| Automated tests | 2 passed |

## 🧪 Testing

The project includes automated tests using **pytest** and **GitHub Actions**.

Run tests locally:

```bash
python -m pytest
