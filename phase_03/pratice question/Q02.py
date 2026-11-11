import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("Dataset/students.csv")

print("\nORIGINAL DATA")
print(df.head())

# 2. Understand dataset
print("\nDATA INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# 3. Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())

# 4. Duplicates
print("\nDUPLICATES")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

# 5. Data cleaning
df["City"] = df["City"].str.strip().str.title()

# 6. Outlier detection using IQR
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Marks"] < lower) |
    (df["Marks"] > upper)
]

print("\nOUTLIERS")
print(outliers)

# 7. Data transformation
df["Performance"] = np.where(
    df["Marks"] >= 80,
    "Good",
    "Needs Improvement"
)

# 8. EDA
print("\nCORRELATION")
print(df.corr(numeric_only=True))

print("\nAVERAGE MARKS")
print(df["Marks"].mean())

print("\nHIGHEST MARKS")
print(df["Marks"].max())

# 9. Data visualization
plt.figure(figsize=(8, 5))

sns.histplot(df["Marks"], bins=5, kde=True)

plt.title("Student Marks Distribution")
plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    hue="Performance"
)

plt.title("Study Hours vs Marks")
plt.show()

plt.figure(figsize=(8, 5))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation")
plt.show()

# 10. Save cleaned dataset
df.to_csv("Dataset/cleaned_students.csv", index=False)

print("\nDATA ANALYSIS COMPLETED!")