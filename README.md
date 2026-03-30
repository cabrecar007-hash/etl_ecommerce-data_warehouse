# ETL Data Warehouse for Multi-Store Log Data

## Project Overview

This project demonstrates a **high-complexity ETL (Extract, Transform, Load) pipeline** that consolidates user activity logs from multiple MySQL databases into a centralized **PostgreSQL data warehouse**. It includes automation, error logging, and analytics-ready reports for business insights.

The pipeline handles large datasets from multiple stores and provides actionable insights such as:

- Total sales per day per store
- Active users per day
- Most common user actions
- Average purchase amount per user

This project is built using Python, PostgreSQL, MySQL, and optionally BigQuery for advanced analytics.

---

## Features

1. **ETL Pipeline**
   - Extract logs from multiple MySQL databases
   - Transform data into a unified schema
   - Load data into PostgreSQL data warehouse
   - Supports incremental loads and ensures data integrity

2. **Automation & Logging**
   - Can be scheduled to run automatically (cron, Airflow, or other scheduler)
   - Logs all ETL runs and errors in `logs/etl.log`
   - Easy to add new stores dynamically

3. **Analytics / Reporting**
   - Predefined SQL queries for key metrics
   - Python scripts to generate CSV reports
   - Dashboard-ready data structure

---

## Technology Stack

- **Databases:** MySQL (source), PostgreSQL (data warehouse)
- **Programming Language:** Python 3.10+
- **Libraries:** `mysql-connector-python`, `psycopg2-binary`, `PyYAML`, `pandas`
- **Optional:** Google BigQuery for analytics

---

## Project Structure

etl_data_warehouse/
├── config/
│ ├── db_config.yaml # MySQL & PostgreSQL connection info
│ └── stores_config.yaml # Store database credentials
├── etl/
│ ├── extract.py # Extract data from MySQL
│ ├── transform.py # Transform data into unified schema
│ ├── load.py # Load data into PostgreSQL
│ └── etl_main.py # Main ETL orchestration
├── analytics/
│ ├── queries.sql # Predefined queries for metrics
│ └── generate_reports.py # Python script to generate reports
├── logs/
│ └── etl.log # ETL run logs
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/etl_data_warehouse.git
cd etl_data_warehouse
```

### 2. Create a Python Virtual Environment

python3 -m venv venv

#### Activate the virtual environment

venv\Scripts\activate

### 3. Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

### 4. Configure Database Connections

#### db_config.yaml

mysql:
  host: 'mysql-host'
  port: 3306
  user: 'username'
  password: 'password'

postgresql:
  host: 'pg-host'
  port: 5432
  user: 'pg_user'
  password: 'pg_password'
  database: 'data_warehouse'

### 5. Run ETL Pipeline

python etl/etl_main.py

### 6. Generate Analytics Reports

python analytics/generate_reports.py

### 7. Adding New Stores

Add the store details to config/stores_config.yaml.
Re-run etl_main.py to include the new store's data in the warehouse.