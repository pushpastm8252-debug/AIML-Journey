import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul", "Priya", "Rahul", "Aman", "Neha"],
    "Age": [20, 21, 20, np.nan, 22],
    "City": ["Delhi", "Mumbai", "Delhi", "delhi", "Delhi"]
}

df = pd.DataFrame(data)

print(df)
print("===clean dataset===")
# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Standardize city names
df["City"] = df["City"].str.title()

print(df)
print("===important function===")
df.duplicated()
df.drop_duplicates()
df.drop_duplicates(subset=["Name"])
df.drop_duplicates(keep="first")
df.drop_duplicates(keep="last")