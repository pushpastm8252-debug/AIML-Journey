print("===series===")
import pandas as pd

marks = pd.Series([85, 90, 78, 95])

print(marks)
print("===data frame===")
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
print("===reading data file===")
df = pd.read_csv("students.csv")
df = pd.read_excel("students.xlsx")
df = pd.read_json("students.json")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)
print(df.dtypes)
print(df.index)