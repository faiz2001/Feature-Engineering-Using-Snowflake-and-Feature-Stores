from snowflake.snowpark import Session
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

# Connection parameters
connection_params = {
    "account": "<your_account>",
    "user": "<your_username>",
    "password": "<your_password>",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "FEATURE_DB",
    "schema": "PUBLIC"
}

session = Session.builder.configs(connection_params).create()

# Load features
df = session.table("FEATURE_DB.PUBLIC.CUSTOMER_FEATURES").to_pandas()

# Example target label (dummy for demonstration)
df["LABEL"] = [1, 0, 1][:len(df)]

# Select features
X = df[["TOTAL_ORDERS", "AVG_ORDER_AMOUNT", "TOTAL_SPENT"]]
y = df["LABEL"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train ML Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save model
with open("trained_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model successfully trained and saved as trained_model.pkl")
