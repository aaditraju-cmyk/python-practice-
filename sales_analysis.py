import pandas as pd

df = pd.read_csv(r"F:\New folder (2)\csv\book.csv")

print(df.head())

# Shape of dataset (rows, columns)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Data types and non-null counts
print(df.info())

# Check missing values
print(df.isnull().sum())

# Option 1: Drop rows with missing values
df_cleaned = df.dropna()

# Option 2: Fill missing values (example: fill with 0)
df_filled = df.fillna(0)

# Average of numerical columns
print("Average values:\n", df.mean(numeric_only=True))

# Highest values
print("Maximum values:\n", df.max(numeric_only=True))

# Lowest values
print("Minimum values:\n", df.min(numeric_only=True))
