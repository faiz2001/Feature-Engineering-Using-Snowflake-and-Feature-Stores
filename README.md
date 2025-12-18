# Feature Engineering with Snowflake & Feature Store

## Project Overview

This project demonstrates an end-to-end machine learning feature engineering pipeline implemented entirely inside Snowflake, including:

Data extraction using SQL

Feature engineering & transformation

Storing features in Snowflake Feature Store

Retrieving features using Snowpark Python

Training an ML model within Snowflake’s compute environment

This setup follows a real-world production ML workflow used by companies to ensure consistency between training and serving features.

## Objectives

✔ Perform feature engineering using SQL
✔ Build an automated, reusable Feature Store
✔ Retrieve features programmatically
✔ Train ML model using Snowpark
✔ Demonstrate an industry-grade ML pipeline

## Tech Stack

| Component       | Technology                         |
| --------------- | ---------------------------------- |
| Data Warehouse  | Snowflake                          |
| Processing      | SQL, Snowpark                      |
| Feature Store   | Snowflake Feature Store            |
| ML Model        | scikit-learn (Logistic Regression) |
| Language        | Python                             |
| Version Control | GitHub                             |

## Architecture

RAW DATA (Snowflake Tables)
        │
        ▼
 SQL Transformations (Feature Engineering)
        │
        ▼
 FEATURE STORE (Snowflake Feature Store)
        │
        ▼
SNOWPARK PYTHON (Feature Retrieval)
        │
        ▼
 ML MODEL TRAINING (Logistic Regression)

## Project Structure

feature-engineering-snowflake/
│
├── sql/
│   ├── create_raw_table.sql
│   ├── insert_sample_data.sql
│   ├── feature_engineering.sql
│   ├── create_feature_store.sql
│   └── load_features.sql
│
├── snowpark/
│   ├── retrieve_features.py
│   └── train_model.py
│
├── docs/
│   └── README_NOTE.txt
│
├── README.md
└── requirements.txt

# Setup Instructions

git clone https://github.com/<your-username>/feature-engineering-snowflake.git
cd feature-engineering-snowflake
