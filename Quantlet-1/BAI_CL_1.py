# Example main code script

import numpy as np
import pandas as pd

# Display full DataFrame output without truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print("\n\n")

# =====================================================
# 1. Load the raw dataset
# =====================================================
df = pd.read_csv("bcn.csv")

print("\n\n")
print(df.head())            # Show first rows
print("\n\n")
print(df.isna().sum())      # Count missing values per column
print("\n\n")
print(df.info())            # Show column types and memory usage


# =====================================================
# 2. Remove unnecessary identifier columns
#    (these columns do not help with modeling or analysis)
# =====================================================
cols_to_remove = {
    "Transaction ID",
    "Item ID",
    "Supplier ID",
    "Customer ID",
    "GPS Coordinates",
    "Transaction Hash"
}

# Only drop columns that actually exist in the dataset
existing_cols = list(set(df.columns) & cols_to_remove)

df.drop(existing_cols, axis=1, inplace=True)

print("\n\n")
print(df.head())   # Show updated dataset after dropping columns


# =====================================================
# (You printed df.head() again here — kept as requested)
# =====================================================
print("\n\n")
print(df.head())


# =====================================================
# 3. Feature engineering from Timestamp column
#    Create weekday, month, year — useful for time-based patterns
# =====================================================

# Reload dataset (your original code did this again — I keep it exactly the same)
df = pd.read_csv("bcn.csv")

# Convert Timestamp → datetime format
df['OrderDateTime'] = pd.to_datetime(df['Timestamp'])

# Add time-based features
df['Weekday_Num'] = df['OrderDateTime'].dt.weekday   # Monday=0 ... Sunday=6
df['Month_Num']   = df['OrderDateTime'].dt.month
df['Year_Num']    = df['OrderDateTime'].dt.year

# Calculate time gap between consecutive transactions
df['TimeGap_Seconds'] = df['OrderDateTime'].diff().dt.total_seconds()

# Remove original timestamp and helper column
df.drop(columns=['Timestamp', 'TimeGap_Seconds'], inplace=True)

print("\n\n")
print(df.head())     # Show dataframe with new features


# =====================================================
# 4. One-hot encode categorical variables
# =====================================================

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Reload dataset again (kept exactly as your original code)
df = pd.read_csv("bcn.csv")

# Columns that should be converted into dummy variables
categorical_cols = ["Smart Contract Status", "Order Status", "Payment Status"]

# Only include columns that actually exist in the dataset
existing_categorical_cols = [col for col in categorical_cols if col in df.columns]

# Encode categorical variables → one-hot dummy variables
df = pd.get_dummies(df, columns=existing_categorical_cols, drop_first=False)

print("\n\n")
print(df.head())     # Check encoding result


# =====================================================
# 5. Groupby analysis: overall averages by Location
# =====================================================
gp = df.groupby("Location")[["Order Amount", "Quantity Shipped", "Quantity Mismatch"]].mean()

print("\n\n")
print(gp)


# =====================================================
# 6. Fraud analysis: Compare metrics for Fraud Indicator = 1
# =====================================================
print("\n\n")
print(
    df[df["Fraud Indicator"] == 1]
    .groupby("Location")[["Order Amount", "Quantity Mismatch"]]
    .mean()
)


# =====================================================
# 7. Fun console messages
#    (kept exactly as your code)
# =====================================================
print("\n\nThis is an Example of a Quantlet")
print("\n\nBatman")


