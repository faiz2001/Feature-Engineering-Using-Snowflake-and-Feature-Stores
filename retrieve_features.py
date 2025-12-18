from snowflake.snowpark import Session
import pandas as pd

# Connection parameters (replace with your credentials)
connection_params = {
    "account": "<your_account>",
    "user": "<your_username>",
    "password": "<your_password>",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "FEATURE_DB",
    "schema": "PUBLIC"
}

# Create Snowpark session
session = Session.builder.configs(connection_params).create()

# Retrieve engineered features
print("Fetching engineered features from Feature Store...")
df = session.table("FEATURE_DB.PUBLIC.CUSTOMER_FEATURES").to_pandas()

print("Feature DataFrame:")
print(df.head())
