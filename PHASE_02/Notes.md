# Phase 02 — Python for Data



Complete Learning Notes

Beginner to Advanced



Is phase mein hum Python ko Data Science aur AI/ML ke liye use karna seekhenge. Main har topic ko English + Hinglish, definitions, syntax, examples, practical programs, important functions, interview questions aur exercises ke saath explain karungi.

Learning goal: Phase 02 complete karne ke baad tum raw data ko handle, clean, analyze, visualize kar paogi aur Machine Learning models ke liye prepare kar paogi.

## 1. Complete syllabus

| No. | Topic        | What you will learn                                   |
| --- | ------------ | ----------------------------------------------------- |
| 01  | API Handling | Requests, JSON, GET, POST, REST API                   |
| 02  | NumPy        | Arrays, dimensions, indexing, mathematical operations |
| 03  | Pandas       | Series, DataFrames, cleaning, filtering, analysis     |
| 04  | Matplotlib   | Charts, plots, labels, customization                  |
| 05  | Seaborn      | Statistical visualization, heatmaps, distributions    |
| 06  | Streamlit    | Interactive Python web applications                   |
| 07  | Scikit-learn | ML preprocessing, training, prediction, evaluation    |

Recommended learning order: API → NumPy → Pandas → Matplotlib → Seaborn → Streamlit → Scikit-learn.

# 01. API Handling

[RESTful API: A Beginner’s Guide to Web APIs](https://images.openai.com/static-rsc-4/O1S21ugbagEbdQqRAUlqLJvXj4rNIbVe2XZ4pIjphmq3kxxKr3NqGRNr-23R0Qi5-CLf_dlu3cty1rYm-AfF-drdkoh_QphcTpXOuR_Q5SuLJ2ih_l96nq0YWAx-17Hu3tCDH9hswFC8jgAnGcuus1nG15d-NMml3ngMYHpIjl8?purpose=inline)

[mailtarget.co](https://mailtarget.co/blog/how-restful-api-works/?utm_source=chatgpt.com)

## 1.1 What is an API?

English Definition: API stands for Application Programming Interface. It allows two different software applications to communicate and exchange data with each other.

Hinglish Explanation: API ek bridge ki tarah kaam karti hai. Iski help se ek application doosri application se data request aur receive kar sakti hai.

Real-life examples:

- Weather app weather server se temperature leti hai.
- Payment application payment gateway se communicate karti hai.
- AI application external API se information receive karti hai.
- Your Python program can fetch data from an online server.

## 1.2 How does an API work?

Client / Python Application

Sends a request

HTTP Request

API / Server

Processes the request

JSON Response

Python Application

Receives and uses data

Example: Suppose you want to get the current weather of Delhi.

1. Python sends a request to a weather API.
2. Server processes the request.
3. Server returns weather information.
4. Python reads and displays the result.

## 1.3 Types of HTTP Methods

| Method | Purpose                  | Hinglish     |
| ------ | ------------------------ | ------------ |
| GET    | Retrieve data            | Data lena    |
| POST   | Send/create data         | Data bhejna  |
| PUT    | Update complete resource | Pura update  |
| PATCH  | Update partial resource  | Thoda update |
| DELETE | Delete data              | Data delete  |

## 1.4 What is JSON?

JSON = JavaScript Object Notation

JSON is a lightweight data format used to exchange information between applications.

Example:

```
{
    "name": "Pushpa",
    "age": 20,
    "skills": ["Python", "NumPy", "Pandas"],
    "is_student": true
}
```

JSON commonly supports:

- Strings
- Numbers
- Booleans
- Arrays
- Objects
- Null

## 1.5 Python API Handling using Requests

First install the library:

```
pip install requests
```

Example program:

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url)print("Status Code:", response.status_code)if response.status_code == 200:    data = response.json()    for user in data:        print(user["name"], user["email"])else:    print("Error:", response.status_code)
```

Line-by-line explanation:

- `import requests`: Imports the Requests library.
- `url`: Stores the API endpoint.
- `requests.get(url)`: Sends an HTTP GET request.
- `response.status_code`: Checks the HTTP response.
- `response.json()`: Converts JSON response into Python objects.
- `for user in data`: Iterates through the received users.

## 1.6 Important HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 429  | Too Many Requests     |
| 500  | Internal Server Error |

## 1.7 Handling API Errors

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"try:    response = requests.get(url, timeout=10)    response.raise_for_status()    data = response.json()    print(data)except requests.exceptions.Timeout:    print("Request timed out")except requests.exceptions.HTTPError as error:    print("HTTP Error:", error)except requests.exceptions.RequestException as error:    print("API Error:", error)
```

Important concepts:

- API Endpoint
- API Key
- Authentication
- Headers
- Query Parameters
- Request Body
- Response
- JSON Parsing
- Timeout
- Rate Limiting

Practical application: Fetch data from an API and store it in a Pandas DataFrame.

# 02. NumPy — Numerical Python

[Numpy Cheatsheet for Beginners–Arrays, Slicing, Reshape, Axis and More - Shuvangkar Das’ Blog](https://images.openai.com/static-rsc-4/cSSuUn2m0ik5cbqxtk0vjxYVZGSc3KRiSJ1PrYDWaOnIk07xDSpazLwIhOUtrGQCoXt8xQF360jFaK68W90KeuiEo-yg1UYvtVyPGWjq9RhnrAs67BFfSQAyjscv_phNZ58hEEyKcJJ2_xkKVw_U9cpCekThjwcPjBjn3BPME4c?purpose=inline)

[3.2.2 Array Basics | AI Roads](https://images.openai.com/static-rsc-4/3OcsXRzVnF-lG3zNU6sJP4whWT2OXTq9J6lMpL4qsbaVpxdJ_REXo3MttMa4lrmAJUdAkD1KAIBd3UWJXqhxzt8rpVge4Xo3ery6saJKdoIrnmkcy9LinGx89_ltWB_bxwDytCY__qkuukYLgmznY7hSG2VqCVqk9DkT4IURFa4?purpose=inline)

[Optimizing Memory Layouts: Avoiding Cache Misses with NumPy Strides | by Thinking Loop | Medium](https://images.openai.com/static-rsc-4/l_MUoXQUkPxjSRNc_YCSXvHDY1aN4NST1kJfj37xrgkkmG3xZiFDKHxWKZzpWq0Me_xpshVfNZ8Epk61Qv88jsZhKJEGnveAITBp38pg52CgIxsPIyy6jZg4n3O6i2257CGQcxq1DgLOioETOEgXrcKpTU0fR4W15SVydhenGtc?purpose=inline)

[Open Science Projects, Coding Tutorials & Research | Moonbooks](https://images.openai.com/static-rsc-4/XoTSJUA2GF7FaFGqMEzd8nRK6WcwIbZTToTsYu0a0y_UOOEa65maFxhplCkjA8NCnij0EfXVRe8RjJujkefLt9D1RUd70gbEhpKlfIvG18LHRpC-YFZ8uwy75XIDsWT8zj3lOApXN-r903xzR6ykICT54uc9BYrFBA1pv4WYiPE?purpose=inline)

[NumPy Arrays | How to Create and Access Array Elements in NumPy?](https://images.openai.com/static-rsc-4/FHhLSOy43ubucHpCMf47YkSwIromjVhM6kJeOaKOhihSYjHpe7OFz6dWfQB3ys2DdkPBEnQUEbQQ8JUNIeOC4ykxy0k-OaDaVHlFLS3jGf8Es_W60BFiJ8me0T2T9TfoJHW3RKfWH_-9fK3lhKqukvIt_1grU2NZUAH_DCZyfbU?purpose=inline)

[NumPy Training | OrcaMinds – Numerical Computing with Python Course Ahmedabad](https://images.openai.com/static-rsc-4/U8k8NJhps03G-f9x7LLTJCAh5NlEpDHWc_lHkFlL4TyYW6gs18SLsG3S3imPlAmxz5Dl0yEPlMKgiMV6S91W9Wwp3YRO32G00i05WGXRQCcSQTx2sL1AahaMftP8XNdMpxfZj8b2OpQudcV5mp_b4TOS5Ahy-a-QDQNBA2KVtKU?purpose=inline)

[Introduction. NumPy stands for Numerical Python… | by Vijayalaxmijanjirala | Dec, 2025 | Medium](https://images.openai.com/static-rsc-4/GzHd-vRsQskkD7ZT7iid0cbOWV33-NbD1ldIFkKf62K3mN-EPnf3xXrzMWIrsCLCplpbsnslWGbcbbKfoULJZsjhwd6hH6K2Yht_xAouOVUaNOHapViiTeeCF5maDeMJBbkCuqK_iRb1cO1J9ClPTD_UOahn1h07iXX50g0ffQ4?purpose=inline)

[NumPy 101: Intro To Numerical Data Manipulation With NumPy + Python | Zero To Mastery](https://images.openai.com/static-rsc-4/c3fto_mfgZHMll3-nFiUz9a4InfrufTzWC2TK1fYu_gOw1DT53hBkc5wjaJOQAz0C2PspTJBo_jvCFDF2d_0LmltqWNq6-WX932V9OOxyJ_H53ZZQByx9ZuWHlPCNs7DLs8hsiWoF5WlmSwyNsUKYSSik4XzCgikNDmDNq1foU4?purpose=inline)

## 2.1 What is NumPy?

English Definition: NumPy stands for Numerical Python. It is a Python library used for numerical computing, mathematical operations, scientific calculations and working with multidimensional arrays.

Hinglish: NumPy ek Python library hai jo large numerical data par fast calculations karne mein help karti hai. Iska main feature `ndarray` hai.

Why use NumPy?

1. Fast mathematical calculations.
2. Multidimensional arrays.
3. Matrix operations.
4. Statistical calculations.
5. Linear algebra.
6. Machine Learning data processing.

## 2.2 Installation and Import

```
pip install numpy
```

```
import numpy as np
```

`np` is the standard alias for NumPy.

## 2.3 What is an Array?

An array is a collection of elements stored in a structured format.

Python list:

```
numbers = [10, 20, 30, 40]
```

NumPy array:

```
import numpy as npnumbers = np.array([10, 20, 30, 40])print(numbers)
```

Output:

```
[10 20 30 40]
```

### Difference between List and NumPy Array

| Python List                           | NumPy Array                     |
| ------------------------------------- | ------------------------------- |
| General-purpose collection            | Numerical computing             |
| Can store mixed data types            | Usually stores one data type    |
| Slower for large numerical operations | Faster for numerical operations |
| No built-in vectorized math           | Supports vectorized math        |

## 2.4 Types of NumPy Arrays

1D Array

```
a = np.array([10, 20, 30, 40])print(a)
```

2D Array

```
b = np.array([    [10, 20, 30],    [40, 50, 60]])print(b)
```

3D Array

```
c = np.array([    [[1, 2], [3, 4]],    [[5, 6], [7, 8]]])print(c)
```

Hinglish:

- 1D = Single row of values.
- 2D = Rows and columns (matrix).
- 3D = Collection of matrices.

## 2.5 Important NumPy Array Attributes

```
import numpy as npa = np.array([    [10, 20, 30],    [40, 50, 60]])print(a.ndim)print(a.shape)print(a.size)print(a.dtype)print(a.itemsize)
```

| Attribute  | Meaning                        |
| ---------- | ------------------------------ |
| `ndim`     | Number of dimensions           |
| `shape`    | Rows and columns               |
| `size`     | Total elements                 |
| `dtype`    | Data type                      |
| `itemsize` | Memory occupied by one element |

Expected output:

```
2
(2, 3)
6
int64
8
```

Note: `dtype` and `itemsize` depend on the system and array type.

## 2.6 Creating NumPy Arrays

```
import numpy as npa = np.array([1, 2, 3])b = np.zeros((2, 3))c = np.ones((3, 3))d = np.full((2, 2), 7)e = np.arange(1, 11)f = np.linspace(0, 10, 5)g = np.eye(3)print(a)print(b)print(c)print(d)print(e)print(f)print(g)
```

Important functions:

| Function              | Purpose                        |
| --------------------- | ------------------------------ |
| `np.array()`          | Create array                   |
| `np.zeros()`          | Create zero array              |
| `np.ones()`           | Create one array               |
| `np.full()`           | Fill with a specific value     |
| `np.arange()`         | Generate a range               |
| `np.linspace()`       | Generate equally spaced values |
| `np.eye()`            | Identity matrix                |
| `np.random.rand()`    | Random values                  |
| `np.random.randint()` | Random integers                |

## 2.7 Array Indexing and Slicing

```
a = np.array([10, 20, 30, 40, 50])print(a[0])print(a[-1])print(a[1:4])print(a[:3])print(a[2:])
```

Output:

```
10
50
[20 30 40]
[10 20 30]
[30 40 50]
```

For 2D arrays:

```
a = np.array([    [10, 20, 30],    [40, 50, 60]])print(a[0, 1])print(a[1, 2])print(a[:, 0])print(a[0, :])
```

Hinglish:

- `a[0,1]` = First row, second column.
- `a[:,0]` = All rows, first column.
- `a[0,:]` = First complete row.

## 2.8 Mathematical Operations

```
a = np.array([10, 20, 30])b = np.array([1, 2, 3])print(a + b)print(a - b)print(a * b)print(a / b)print(a ** 2)
```

Output:

```
[11 22 33]
[ 9 18 27]
[10 40 90]
[10. 10. 10.]
[100 400 900]
```

These operations are called vectorized operations.

Hinglish: Loop lagaye bina complete array ke elements par operation perform karna vectorization kehlata hai.

## 2.9 NumPy Statistical Functions

```
data = np.array([10, 20, 30, 40, 50])print(np.sum(data))print(np.mean(data))print(np.median(data))print(np.min(data))print(np.max(data))print(np.std(data))print(np.var(data))
```

| Function          | Meaning            |
| ----------------- | ------------------ |
| `np.sum()`        | Sum                |
| `np.mean()`       | Average            |
| `np.median()`     | Middle value       |
| `np.min()`        | Minimum            |
| `np.max()`        | Maximum            |
| `np.std()`        | Standard deviation |
| `np.var()`        | Variance           |
| `np.percentile()` | Percentile         |

## 2.10 Reshaping and Joining

```
a = np.arange(1, 7)b = a.reshape(2, 3)print(b)
```

Output:

```
[[1 2 3]
 [4 5 6]]
```

Joining arrays:

```
a = np.array([1, 2])b = np.array([3, 4])print(np.concatenate((a, b)))
```

Other important functions:

- `reshape()`
- `flatten()`
- `ravel()`
- `transpose()`
- `concatenate()`
- `vstack()`
- `hstack()`
- `split()`
- `sort()`
- `unique()`
- `where()`

## 2.11 Broadcasting

Definition: Broadcasting allows NumPy to perform operations between arrays of different shapes when their dimensions are compatible.

```
a = np.array([10, 20, 30])print(a + 5)
```

Output:

```
[15 25 35]
```

Here, NumPy automatically adds 5 to every element.

## 2.12 Random Number Generation

```
rng = np.random.default_rng(42)print(rng.random(5))print(rng.integers(1, 100, size=5))print(rng.normal(0, 1, size=5))
```

`default_rng()` is the recommended modern random generator.

## 2.13 Linear Algebra

```
a = np.array([    [1, 2],    [3, 4]])b = np.array([    [5, 6],    [7, 8]])print(np.dot(a, b))print(np.linalg.det(a))print(np.linalg.inv(a))print(np.linalg.eig(a))
```

Important:

- Dot product
- Matrix multiplication
- Determinant
- Inverse
- Eigenvalues
- Eigenvectors

NumPy applications in AI/ML:

- Numerical calculations.
- Feature transformations.
- Matrix operations.
- Image processing.
- Model computations.
- Mathematical foundations of neural networks.

### NumPy Practice Questions

1. Create a 1D array containing 20 numbers.
2. Create a 3×3 matrix.
3. Find the mean, median and standard deviation.
4. Extract the second row from a matrix.
5. Convert a 1D array into a 2D array.
6. Find the maximum and minimum values.
7. Perform matrix multiplication.

# 03. Pandas — Data Analysis and Manipulation

[A Gentle Visual Intro to Data Analysis in Python Using Pandas – Jay Alammar – Visualizing machine learning one concept at a time.](https://images.openai.com/static-rsc-4/VikRJWb15dVV8UWRwqkNv6VDYamurcTSOv1NNIjIgvHut4IEuWR_knNvkUOTPCyxwswuXI0JXLcAZo4N9RKldB8YsLt-_d2JZ7MFrahNi2BkcnbF4xejxmUulR3zarZtu93URaBDpUGeIyWQkIO1SgnFPecLlFUvlsTCJBmt940?purpose=inline)

[jalammar.github.io](https://jalammar.github.io/gentle-visual-intro-to-data-analysis-python-pandas/?utm_source=chatgpt.com)

## 3.1 What is Pandas?

English Definition: Pandas is an open-source Python library used for data manipulation, data cleaning, data analysis and working with structured datasets.

Hinglish: Pandas ka use data ko read, clean, organize, filter aur analyze karne ke liye hota hai. Agar tumhare paas CSV ya Excel file hai, toh Pandas se usko easily handle kar sakti ho.

Real-world example: Student dataset:

| Name | Age | Marks | City   |
| ---- | --- | ----- | ------ |
| A    | 20  | 85    | Meerut |
| B    | 21  | 90    | Delhi  |
| C    | 19  | 75    | Noida  |

Pandas is used to analyze this information.

## 3.2 Installation

```
pip install pandas
```

```
import pandas as pd
```

`pd` is the standard alias.

## 3.3 Main Data Structures

Pandas has two major data structures:

### A. Series

A Series is a one-dimensional labeled array.

```
import pandas as pdmarks = pd.Series([85, 90, 75, 95])print(marks)
```

### B. DataFrame

A DataFrame is a two-dimensional table with rows and columns.

```
data = {    "Name": ["Aman", "Riya", "Rahul"],    "Age": [20, 21, 19],    "Marks": [85, 90, 75]}df = pd.DataFrame(data)print(df)
```

Difference:

| Series                | DataFrame                 |
| --------------------- | ------------------------- |
| 1D                    | 2D                        |
| Single labeled column | Multiple rows and columns |
| Single data series    | Tabular data              |

## 3.4 Reading Different File Formats

```
df = pd.read_csv("students.csv")df = pd.read_excel("students.xlsx")df = pd.read_json("students.json")df = pd.read_sql("SELECT * FROM students", connection)
```

File types:

- CSV
- Excel
- JSON
- SQL database

## 3.5 Understanding Dataset

```
print(df.head())print(df.tail())print(df.shape)print(df.columns)print(df.index)print(df.dtypes)print(df.info())print(df.describe())
```

| Function     | Purpose             |
| ------------ | ------------------- |
| `head()`     | First five rows     |
| `tail()`     | Last five rows      |
| `shape`      | Rows and columns    |
| `columns`    | Column names        |
| `index`      | Row labels          |
| `dtypes`     | Data types          |
| `info()`     | Dataset summary     |
| `describe()` | Statistical summary |

You can change the number of rows:

```
df.head(10)df.tail(3)
```

## 3.6 Selecting Columns and Rows

```
print(df["Name"])print(df[["Name", "Marks"]])print(df.loc[0])print(df.iloc[0])print(df.loc[0, "Name"])print(df.iloc[0, 2])
```

Difference between loc and iloc:

- `loc` uses row and column labels.
- `iloc` uses integer positions.

Example:

```
print(df.loc[0:2, ["Name", "Marks"]])print(df.iloc[0:2, 0:2])
```

## 3.7 Filtering Data

```
high_marks = df[df["Marks"] > 80]print(high_marks)
```

Multiple conditions:

```
result = df[    (df["Marks"] > 80) &    (df["Age"] >= 20)]print(result)
```

Operators:

| Operator | Meaning      |
| -------- | ------------ |
| `&`      | AND          |
| `\\|`    | OR           |
| `~`      | NOT          |
| `>`      | Greater than |
| `<`      | Less than    |
| `==`     | Equal to     |
| `!=`     | Not equal to |

Additional filtering:

```
df[df["City"].isin(["Delhi", "Meerut"])]df[df["Name"].str.contains("A", case=False)]
```

## 3.8 Handling Missing Values

Missing values are common in real-world datasets.

Example:

| Name  | Marks |
| ----- | ----- |
| Aman  | 80    |
| Riya  | NaN   |
| Rahul | 90    |

`NaN` means Not a Number and is commonly used to represent missing numerical data.

Check missing values:

```
print(df.isnull())print(df.isnull().sum())
```

Remove missing values:

```
df.dropna()
```

Fill missing values:

```
df["Marks"] = df["Marks"].fillna(    df["Marks"].mean())
```

Other methods:

```
df.fillna(0)df.ffill()df.bfill()
```

Important: Missing data should be handled according to the meaning of the column. Filling every missing value with zero is not always correct.

## 3.9 Removing Duplicates

```
print(df.duplicated())df.drop_duplicates(inplace=True)
```

Hinglish: Agar dataset mein same record multiple times present hai, toh duplicates remove karne ke liye use karte hain.

## 3.10 Adding, Updating and Deleting Columns

Add column:

```
df["Grade"] = ["A", "A+", "B"]
```

Update column:

```
df["Marks"] = df["Marks"] + 5
```

Delete column:

```
df.drop(columns=["Grade"], inplace=True)
```

Rename column:

```
df.rename(    columns={"Marks": "Score"},    inplace=True)
```

## 3.11 Sorting Data

```
df.sort_values(    by="Marks",    ascending=False)
```

- `ascending=True`: Small to large.
- `ascending=False`: Large to small.

## 3.12 GroupBy Operations

GroupBy is used to group data according to a specific column.

Example:

```
data = {    "Department": ["CSE", "CSE", "AI", "AI"],    "Marks": [80, 90, 85, 95]}df = pd.DataFrame(data)result = df.groupby("Department")["Marks"].mean()print(result)
```

Output:

```
Department
AI     90.0
CSE    85.0
```

Important GroupBy operations:

```
df.groupby("Department").sum()df.groupby("Department").mean()df.groupby("Department").count()df.groupby("Department").max()df.groupby("Department").min()
```

## 3.13 Merge, Join and Concatenate

These are important when working with multiple datasets.

Concatenate:

```
pd.concat([df1, df2])
```

Merge:

```
pd.merge(    df1,    df2,    on="Student_ID",    how="inner")
```

Join:

```
df1.join(df2)
```

Difference:

| Operation     | Purpose                              |
| ------------- | ------------------------------------ |
| Concatenation | Combine rows or columns              |
| Merge         | Combine using common columns or keys |
| Join          | Combine primarily using indexes      |

## 3.14 Apply and Map

```
df["Marks"].apply(lambda x: x + 5)
```

Mapping:

```
grade_map = {    "A": "Excellent",    "B": "Good"}df["Description"] = df["Grade"].map(grade_map)
```

## 3.15 Date and Time Handling

```
df["Date"] = pd.to_datetime(df["Date"])df["Year"] = df["Date"].dt.yeardf["Month"] = df["Date"].dt.monthdf["Day"] = df["Date"].dt.day
```

## 3.16 Exporting Data

```
df.to_csv("output.csv", index=False)df.to_excel("output.xlsx", index=False)df.to_json("output.json")
```

## 3.17 Complete Pandas Mini Project

Project: Student Performance Analysis

```
import pandas as pddata = {    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],    "Maths": [80, 90, 75, 95, 60],    "Science": [85, 88, 80, 92, 65],    "English": [78, 95, 70, 90, 75]}df = pd.DataFrame(data)df["Total"] = df[    ["Maths", "Science", "English"]].sum(axis=1)df["Average"] = df[    ["Maths", "Science", "English"]].mean(axis=1)df["Result"] = df["Average"].apply(    lambda x: "Pass" if x >= 40 else "Fail")print(df)print("\nTop Student:")print(df.loc[df["Average"].idxmax()])print("\nClass Average:")print(df["Average"].mean())
```

What you learn:

- Creating a DataFrame.
- Adding new columns.
- Calculating totals and averages.
- Applying conditions.
- Finding the top-performing student.
- Statistical analysis.

# 04. Matplotlib — Data Visualization

[Matplotlib Subplot 활용해서 그래프 여러개 그리는 3가지 방법](https://images.openai.com/static-rsc-4/f90FI6V1TNUIHLkmKpddhro7yLANqgXfAcnZlySJ7JD2EjzCfPomDdSbxoCeaP3X1F4kpuVwhwKMA19YS2Jrz6JrtElvPHaWt-AdoCPMPu7EzIlZ5PEBDI9IQen-TDYGizU11kGNwHz6u5a6g-Udkupwn5OuZ6yEV6-qKbHGaf0?purpose=inline)

[3. Gráficos com Matplotlib — \<h2 style="color:#cc0000;">\<b>Introdução à Visualização de Dados\</b>\</h2>\<p style="font-size:80%;color:#cc0000;">com Python\</p>](https://images.openai.com/static-rsc-4/jliegm2Dz19PucPlU6hzxu_5Vsc84UeswRkUTVNU2RAPlQI9mLADWoxr6nt4dZrPLIaSWuolKLgjz3UFFndL4UJK_clEbtrrVEyfkH7X_a3AKEiu9bXQmR3k6mRM-wo5XZw9TYEHGEG2XELc5n0ulIkCZJq2PM8wS3SVk9KyRbM?purpose=inline)

[Data Visualization using Matplotlib - Data Science and ML](https://images.openai.com/static-rsc-4/uqQzBu-7g6vYyCopzGlQOtFIxuGl13u_XQBOYUWD3BJUGiTAPZoP1h6rd4BLigr-XQO1v0S0ePtr66D75iRTpsp41d5GEMc09UukL8PoJOe5jy56ZgkuS29pFkzGpB6BkR0Cp6wpSljDrrsPLiqrWpeD2TddBx_Ar-C6mkiJXnU?purpose=inline)

[Matplotlib Subplot 활용해서 그래프 여러개 그리는 3가지 방법](https://images.openai.com/static-rsc-4/IN0l4qqsy0ajFCfoe7GznoRNQnbm9eFSTwHqh5uwzC5ZBx_-Iolz7kLAUeRS3N6CpQy-u18RjUwez1Ubud9aD6hkDaig72WYyGCk-xn0xqKyuhzB0GlKxfXBpKiC-32RAs1chk1RqpjxlyEh_cI4WDVkwqyTC89DptZ1hjEhnhc?purpose=inline)

[Aprenda Desafio 2: Outros Tipos de Gráficos | Matplotlib](https://images.openai.com/static-rsc-4/V_B0MayvJSsqoNwIYo3kk6EHTmaAcRLfIb-TvCWkLEGhp_VAYqiBMJkFmAXrMaGsD7Qrt1_t6imVL5og8HjIqJiDU2clLDk2DpQzgkZCqvZq-LUxM36QPSvDBRypCiffsXqzkK6ZoNs_RJPmr3UI8-s01G_czwmM1ToLzlBA5IY?purpose=inline)

[Manipulating Data Part 1: Using Matplotlib to display plots | by MORGAN KATZ | Medium](https://images.openai.com/static-rsc-4/IpAOxyNmuMlLT7Pb8zeUUoqsqkhBYL32kqjsJcwmgO2mu0ZmXh7i1G38wrsB0ydOeXf9TDqFRK3lJ_tP1rxCxAFQRdBV_OfjobOfi7qS5gAYzk_z45JYM6b42Xb8jEHeFf4IuVquRSk0_gs6JOxpllcHEYMSvHWYgwfgOZA4_5I?purpose=inline)

[Mastering Data Visualization in Python with Matplotlib](https://images.openai.com/static-rsc-4/49Gv8q0xHGaBUaAM95GnNXzxN4RwwMpzAFFaYiFzCcG6XJ0E_6GSSRFcgBiGR_63_GZM0oSvAISUMrlc3ddMpk267RKLbT3GastSWVDhqg8wN0RF79M86XT18X73A96N24_pvwf0ciUUfC-Q886TXehT7Hrze3e71KPnlZUR6JA?purpose=inline)

[Your Career in Data Analytics and Data Science Starts Here | Resagratia](https://images.openai.com/static-rsc-4/RAWg2bscKv73Ws-zp9wfT7rJEDZPIxhbGSBv9JV2toNibncQMSdujoNsGtSVK00tGYWXws_HE_FB-bHDeZc21RgEsLyj1bkGc-qrqqV1GnYIhREvfyWWqj63O3gBSHFIWN6rGrZeO7jRM88sWjEysPC_GWnEdnYU4uRN4gx0L5I?purpose=inline)

[Matplotlib vs. Plotly: Choosing the Right Data Visualization Tool](https://images.openai.com/static-rsc-4/-85Qggfc-04J9v_h8YLF303SajUOu6QACjEOCF0YWVeik_XRoH4vRRQpDPrFoMdNtjswwX6POqNJ3d38oTDcSk0PjKUzskGzKj3JcuCb-7XcKlBmq2JM-Wq9-8TUqGYK8zj2Qtfh0Y3HKFydOLyNmGqpjH-N-0btmbm9NyXLLJI?purpose=inline)

## 4.1 What is Matplotlib?

English Definition: Matplotlib is a Python data visualization library used to create graphs, charts and plots from numerical and categorical data.

Hinglish: Matplotlib ka use data ko graphs aur charts mein convert karne ke liye hota hai. Isse hum data ko visually understand kar sakte hain.

Examples:

- Student marks comparison.
- Monthly sales analysis.
- Temperature trends.
- Model accuracy comparison.
- Data distributions.

## 4.2 Installation

```
pip install matplotlib
```

Import:

```
import matplotlib.pyplot as plt
```

`plt` is the standard alias for `pyplot`.

## 4.3 Line Plot

A line plot displays trends or changes over time.

```
import matplotlib.pyplot as pltdays = [1, 2, 3, 4, 5]marks = [50, 60, 65, 80, 90]plt.plot(days, marks)plt.title("Student Performance")plt.xlabel("Days")plt.ylabel("Marks")plt.show()
```

Hinglish: Jab hume dekhna ho ki time ke saath values kaise change ho rahi hain, tab line plot use karte hain.

## 4.4 Bar Chart

Used to compare different categories.

```
subjects = ["Python", "Java", "C++"]marks = [90, 80, 75]plt.bar(subjects, marks)plt.title("Subject Marks")plt.xlabel("Subjects")plt.ylabel("Marks")plt.show()
```

Horizontal bar chart:

```
plt.barh(subjects, marks)plt.show()
```

## 4.5 Scatter Plot

Used to understand relationships between two numerical variables.

```
hours = [1, 2, 3, 4, 5]marks = [40, 50, 65, 75, 90]plt.scatter(hours, marks)plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Study Hours vs Marks")plt.show()
```

## 4.6 Histogram

A histogram shows the frequency distribution of numerical data.

```
marks = [40, 45, 50, 55, 60, 65, 70, 75, 80, 90]plt.hist(marks, bins=5)plt.title("Marks Distribution")plt.xlabel("Marks")plt.ylabel("Frequency")plt.show()
```

## 4.7 Pie Chart

A pie chart displays proportions of a whole.

```
subjects = ["Python", "Java", "C++"]values = [40, 30, 30]plt.pie(    values,    labels=subjects,    autopct="%1.1f%%")plt.title("Learning Distribution")plt.show()
```

## 4.8 Box Plot

Used to understand data distribution and identify potential outliers.

```
marks = [45, 50, 55, 60, 65, 70, 75, 100]plt.boxplot(marks)plt.title("Marks Distribution")plt.show()
```

## 4.9 Important Plot Customization

```
plt.plot(    [1, 2, 3, 4],    [10, 20, 30, 40],    color="blue",    marker="o",    linestyle="--",    linewidth=2,    label="Sales")plt.title("Sales Report", fontsize=16)plt.xlabel("Month")plt.ylabel("Sales")plt.legend()plt.grid(True)plt.savefig("sales_chart.png")plt.show()
```

Important functions:

| Function         | Purpose        |
| ---------------- | -------------- |
| `plot()`         | Line graph     |
| `bar()`          | Vertical bar   |
| `barh()`         | Horizontal bar |
| `scatter()`      | Scatter plot   |
| `hist()`         | Histogram      |
| `pie()`          | Pie chart      |
| `boxplot()`      | Box plot       |
| `title()`        | Chart title    |
| `xlabel()`       | X-axis label   |
| `ylabel()`       | Y-axis label   |
| `legend()`       | Show legend    |
| `grid()`         | Grid lines     |
| `subplot()`      | Multiple plots |
| `savefig()`      | Save chart     |
| `show()`         | Display chart  |
| `figure()`       | Create figure  |
| `tight_layout()` | Adjust spacing |

## 4.10 Subplots

Subplots allow multiple charts in one figure.

```
import matplotlib.pyplot as pltfig, axes = plt.subplots(1, 2)axes[0].plot([1, 2, 3], [10, 20, 30])axes[0].set_title("Line Plot")axes[1].bar(    ["A", "B", "C"],    [20, 40, 60])axes[1].set_title("Bar Chart")plt.tight_layout()plt.show()
```

Matplotlib in Machine Learning:

- Visualize training results.
- Compare model accuracy.
- Plot loss curves.
- Analyze distributions.
- Visualize predictions.

# 05. Seaborn — Statistical Data Visualization

[Unlocking Insights with Heatmaps: Correlation Analysis in Data Visualization | CodeSignal Learn](https://images.openai.com/static-rsc-4/q0mvOAQi1Hem7apER-f48ubF9xOql85hXw1ssxAY02G9ADTpaFRFhIcLqFAe6qxvU8u4YZRnibc56bWup_SL4w9we6TD4VTMVt7AAzUwdKsa_REVscaLd9HlKm7mc-PTqTnOxtmdLYOyWT9MlWYOhNaOqp-nXl8ljHWEmVPWGEw?purpose=inline)

[seaborn.pairplot — seaborn 0.13.2 documentation](https://images.openai.com/static-rsc-4/nqS24YtpO3Dyr2Xi4M1_5gueKaIcNYZOFgZw7AwyCS2T_UWjjLcrHwuKPBxF1iyvxPodhC6kc3C0W-z7HTWTbZ2sGeF3yh7JZ06nOEp0HLoCtM47jjQPh_Eay-9ZzbnatqGTm96jE9msOh7xKczH7b7G9kwucGArad92YLYeI40?purpose=inline)

[Various Plot types in Seaborn. Categorical Data | by Ravjot Singh | Analytics Vidhya | Medium](https://images.openai.com/static-rsc-4/TZmQ7bu-odKk2dRZEcx3j8o3vz2gcDWAU12f9wS5ruqJaKtaBAY7p29VtZ7dJnDRcN8Ey8Vd1o8nC40BV9JLil7Rsaea4KIWalIyBXZV5H6PvXiBXKo1xRBtc31ZeUKe496ynRz5FM-bNNsXrtapcP_ZVXsE4hj2Pu0LBbrb1vk?purpose=inline)

[Exploratory Data Analysis on Iris Dataset – Data Brains](https://images.openai.com/static-rsc-4/lnajxJgGntHMHNdCEVQxwu3XESz_Bq3YooXqMP5ky0jZ5hY9_NJZ0QbhB0Rf6B037zscao3DfoTS93YW_Qg5vs3eAJqvEgl9Cfc91qy-BSFnJyFpZfkWVUq0AmruEMEoGm9WiwUlJ8DLXoBlBAvZvVABzhK-HLA2V6opDzSdeQU?purpose=inline)

[A Complete Guide to Plotting Categorical Variables with Seaborn | by Will Norris | TDS Archive | Medium](https://images.openai.com/static-rsc-4/FWJ-EhchWTDILoketlXYXedqQoOepWOUGF6EB9qtyc9aYaB7Xeh-FcgQQIncfB4Wka4yQcb1Z1d1wURD6hyEaOCBN968DDJAYoD-3IaKXJL3MhRVm2ufwJOOuX22IX3Ecw93FoC6M-wJJMRg6zSpkFTnJ014lyFzLVUY0cvLGAQ?purpose=inline)

[Jupyter-Notebook ile Veri Analizi (Bölüm 2) | by M. W. Ugur | Medium](https://images.openai.com/static-rsc-4/EyzuedlMAHi-bJHHjajiKsSYYFdGTgbQgsL7okZYeAZFy_ze7PW4bCNzzcNJ_qGvtTBfKrUKtwMUduu6moDfg5NAnDvGp4rPSxoX2e5UGwHFhxAlVBtS4nwFuzYrSk1YEjEF4RVJ8421kktPfIxpBdPEVyBRzMcxOi6qlsCGfkw?purpose=inline)

## 5.1 What is Seaborn?

English Definition: Seaborn is a Python statistical data visualization library built on top of Matplotlib. It provides attractive and informative statistical graphics.

Hinglish: Seaborn Matplotlib ke upar built library hai. Iska use advanced aur beautiful statistical graphs banane ke liye hota hai. Data ke patterns, relationships, distributions aur correlations ko easily understand kar sakte hain.

## 5.2 Why use Seaborn?

1. Attractive statistical graphs.
2. Better default styling.
3. Easy DataFrame integration.
4. Correlation analysis.
5. Distribution visualization.
6. Categorical data analysis.

## 5.3 Installation

```
pip install seaborn
```

Import:

```
import seaborn as snsimport matplotlib.pyplot as plt
```

## 5.4 Understanding Dataset with Seaborn

Seaborn provides built-in sample datasets.

```
import seaborn as snsdf = sns.load_dataset("tips")print(df.head())print(df.info())print(df.describe())
```

The `tips` dataset contains restaurant bill and tip information.

## 5.5 Line Plot

```
sns.lineplot(    data=df,    x="size",    y="total_bill")plt.title("Bill vs Group Size")plt.show()
```

## 5.6 Bar Plot

```
sns.barplot(    data=df,    x="day",    y="total_bill")plt.title("Average Bill by Day")plt.show()
```

A Seaborn bar plot generally displays an estimated statistic, mean by default, with an uncertainty interval.

## 5.7 Scatter Plot

```
sns.scatterplot(    data=df,    x="total_bill",    y="tip",    hue="sex",    style="time")plt.title("Bill vs Tip")plt.show()
```

Important parameters:

- `x`: X-axis variable.
- `y`: Y-axis variable.
- `hue`: Different colors based on category.
- `style`: Different marker styles.
- `size`: Different marker sizes.

## 5.8 Histogram and KDE Plot

```
sns.histplot(    data=df,    x="total_bill",    bins=20,    kde=True)plt.show()
```

KDE = Kernel Density Estimation

KDE creates a smooth curve representing the estimated distribution of numerical data.

Hinglish: Histogram frequency batata hai aur KDE data ka smooth distribution pattern show karta hai.

## 5.9 Box Plot

```
sns.boxplot(    data=df,    x="day",    y="total_bill")plt.show()
```

Used for:

- Median.
- Quartiles.
- Data spread.
- Potential outliers.

## 5.10 Violin Plot

```
sns.violinplot(    data=df,    x="day",    y="total_bill")plt.show()
```

A violin plot combines a box-plot-like summary with a distribution density shape.

## 5.11 Count Plot

```
sns.countplot(    data=df,    x="day")plt.show()
```

Used to count observations in each category.

## 5.12 Heatmap — Very Important for AI/ML

[Beginner’s Guide to ML with the Titanic Dataset: Step by Step Intuition with Code | by Subhoshripal | Medium](https://images.openai.com/static-rsc-4/1bj561gH7SBvbLsyWxoCwgtouyBcFXgrwc_nPnD1Yabt63bvcnaBibMZdaEYAtvZEuCsNG65_h3TeBpjACmeg3qrROZD-BX6KRwAkxXsK1a-2ybdg-XlnoFps6Yqe3iKFcdvpw32c4287MehrZBd0hqmHtZzuYbcEjuxqPTHtgQ?purpose=inline)

[medium.com](https://medium.com/%40subhoshripal/beginners-guide-to-ml-with-the-titanic-dataset-step-by-step-intuition-with-code-09ca2f851b02?utm_source=chatgpt.com)

A heatmap displays numerical values using colors.

Correlation: Correlation measures the strength and direction of the relationship between two numerical variables.

```
import seaborn as snsimport matplotlib.pyplot as pltdata = {    "Study_Hours": [1, 2, 3, 4, 5],    "Marks": [40, 50, 65, 75, 90],    "Sleep_Hours": [8, 7, 7, 6, 6]}df = pd.DataFrame(data)correlation = df.corr(numeric_only=True)sns.heatmap(    correlation,    annot=True,    cmap="coolwarm")plt.title("Correlation Heatmap")plt.show()
```

Correlation values:

| Value | Meaning                      |
| ----- | ---------------------------- |
| +1    | Perfect positive correlation |
| 0     | No linear correlation        |
| -1    | Perfect negative correlation |

Important: Correlation does not prove causation.

## 5.13 Pair Plot

```
sns.pairplot(    df,    diag_kind="hist")plt.show()
```

Pairplot shows relationships between multiple numerical columns.

Useful for exploratory data analysis (EDA).

## 5.14 Joint Plot

```
sns.jointplot(    data=df,    x="Study_Hours",    y="Marks",    kind="scatter")plt.show()
```

Shows a relationship plot along with individual distributions.

## 5.15 Seaborn Important Functions

| Function            | Purpose                         |
| ------------------- | ------------------------------- |
| `sns.lineplot()`    | Line plot                       |
| `sns.barplot()`     | Statistical bar chart           |
| `sns.scatterplot()` | Scatter plot                    |
| `sns.histplot()`    | Histogram                       |
| `sns.kdeplot()`     | Density curve                   |
| `sns.boxplot()`     | Box plot                        |
| `sns.violinplot()`  | Violin plot                     |
| `sns.countplot()`   | Category counts                 |
| `sns.heatmap()`     | Heatmap                         |
| `sns.pairplot()`    | Multiple variable relationships |
| `sns.jointplot()`   | Joint distribution              |
| `sns.regplot()`     | Regression visualization        |
| `sns.catplot()`     | Categorical plots               |
| `sns.set_theme()`   | Set visual theme                |

## 5.16 Matplotlib vs Seaborn

| Matplotlib                     | Seaborn                           |
| ------------------------------ | --------------------------------- |
| General visualization library  | Statistical visualization library |
| More manual customization      | Attractive defaults               |
| Works with lists and arrays    | Integrates well with DataFrames   |
| Lower-level control            | Higher-level plotting interface   |
| More control over plot details | Convenient statistical plots      |

Interview question: Is Seaborn dependent on Matplotlib?

Answer: Yes. Seaborn is built on top of Matplotlib and uses Matplotlib for rendering many of its visualizations.

# 06. Streamlit — Build Web Applications with Python

[The Art of Creating Dashboard Apps | by Chanin Nantasenamat | Data Professor | Medium](https://images.openai.com/static-rsc-4/3fAOS64Ii2aML1KSeQFbdiSpk0rlMeXxzXuYrSW55mTpHcJ9iiOP6Ou-ku41fLBNCwVK3i55TyAtL4Pm1RG6iiUwRcu9wmO2-YqdyE4OrdIR2JjD10bVsWajbV6HUcgOMVkrhnvqNiLpHkplOnxxm6TeH862Fan5EPk7FQH8-Ds?purpose=inline)

[A Custom interactive Machine Learning Dashboard using Streamlit | Upwork](https://images.openai.com/static-rsc-4/0es3Jl-REXQLw08q9XVZxWh5zL135MDSJrjDKqfu-bzZ7BSgdiQLy3OnQWTerCXRkZlRKw0-T8X2MpQEfhKPzydzr6KrE6l0lEATKr3bj4CTCI8FwcLRMq3uqnwp_qcZ_8x6o0uudPa-hcqvnz7U5CePwRKQQyIFfBIk3T8V66I?purpose=inline)

[Unified Mentor | LinkedIn](https://images.openai.com/static-rsc-4/BopTLLxXmR0HGhYjANs991iAvRYP443iW-rFeRZj8c34OHGdP_8kIQPQwhnBlRLF-vyNAY6gJKU5PqLH4ic7olCAL-Aay0xzz5MxXWy_c5yvid9iy4nWlGbOxxX-FGg71QvvPvX4T0zYg3HIojCAzx-0-JtJcQcqqmikVHNr9pQ?purpose=inline)

[Streamlit • A faster way to build and share data apps](https://images.openai.com/static-rsc-4/nuINzlCe0L5sngb5qcC62X35WTsfTHlD1zG_gnKMmx7BHG70BxRxkBiUvlmFTM_apGpCN8JY--XHEhaGnDhWXxs2EmuTg9SLuAsLj8d7mUP5IHX-wBLJjMQwh-T8uKhWQqXZqHJZTcpdyxrslyOy0Wfl42aYrtnrioXPsw3YHk0?purpose=inline)

[A Custom interactive Machine Learning Dashboard using Streamlit | Upwork](https://images.openai.com/static-rsc-4/2YBXe5LWDRc1Ai5krYB-JyrtvF_y9j7sZSE4fzFQmtYxwbz5qoy_H2DlkfTTjGrLcoT5sRn8QSFQc4RiY7RhktmAEFy9EGZuRdi5lZyAsdQyI3ovtO09OxJ2r1i3Zp-GA47ZBSEYWbA6fe28wNc8tCS0vPQAbRhyVa0GWMr_nUc?purpose=inline)

[GitHub - Ryanakml/Reinforcement-Learning-Concept-and-Implementation · GitHub](https://images.openai.com/static-rsc-4/_nSypofvxtlG05LB9DAhizPA37tphzPImhOoNM2FLxRUZdrF0Kz56KUDS6YLNgFafrxB8I70-02tGm30vrvHV5noX06-Rifg66DW1EcG79jGvOw6yKb_LuVbl9Kz7xhYtbxOO8AqW2MM_fAxGN4ccHUeNOltd-tSHTymmV-zLyg?purpose=inline)

[#streamlit #sparklines #dashboard #python | Chanin Nantasenamat | 10 comments](https://images.openai.com/static-rsc-4/uM6qhgRnB31yoCRQF9SUg0jRfGux_vblEwx2cHJdUXGIFTMxQjdZPhwr6n6ChA5KcqV7q_A870ru9NHInyEVJwD_PWustXlSU2VmrEiw8eXEBJfQSD2_erw8SG_tcP3whNH4DSTb4CsNXsy7ALy8Ay_lGVIaPgetV7fD6Gn3Qe8?purpose=inline)

[A beautiful platform for data visualization and machine learning | Upwork](https://images.openai.com/static-rsc-4/Rvu6S-Eoe3jT3_ETtPaGEg87e-I9m8jOQIS1Uq8wtQ7us1vrbIhNZEj9Dyul8trsM7LNCJoiyfuyAiobj1vxxuyRPubE_eEGxQ3vrIsKr7797eulpeQxfeuI5d6cA8TjqXxcXUXl6LLoCcrHWcPb0jQ8tZFrqfS1_04Ij3-3-U4?purpose=inline)

[Building a Complete E-Commerce Analytics Platform: From Customer Segmentation to Shopify Monetization | by Timothy Kimutai | Medium](https://images.openai.com/static-rsc-4/Nd21fzL3MB4Gx_VHK_ky9ZYGaVDyPFmGYl0nwncPXO1TadHRYWuEuXZKtZSlfGJV1Kvwi1FPnhPJND_bi9SzEfdooKuvf7Z39vuRWW_2qh5LkY2bvq14BKGUYSVgQ202fKo2IVZxNtvZlG2j1ozKwRw_LazLDSGPr-pxjq-5njs?purpose=inline)

[Streamlit Application for Credit Card Fraud Detection | Upwork](https://images.openai.com/static-rsc-4/8XZfQOT-jzc6dLkJtVtYVAjHuPKYO2t9QVUg2ljgAZjOtDVLEM3Z9TeWxicPtuW71SkJ9dgbP5EHu0BqP1-Uw6SB34OiOIFLfkJFfPJJKrJK9sZhSsYT9gnQ_2e9VpPDq__WOfUwSPUwApCnTJ7HTsullCDeYR9TRwlef5_EFPM?purpose=inline)

[GitHub - Paras-bakshi/Titanic-Survival-Rate-Dashboard: Dashboard of Exploratory Data Analysis of Titanic Dataset using Streamlit](https://images.openai.com/static-rsc-4/Z0bO5ZTB7DTBmVMwMQxSMBaluQKNQL4NcskJ2ghGqY1FhEpDo7iyzKIB0gtrynzpzBs2Jd_RHDEdLrhLqGBM88hhRMdlMUzN4of4725gXidpR9SP7nd2M4fI-GUBh1Z5ECgnw7TrSUm_5APyAtD8h1aNkVO6-IhDZuB_kku3uyY?purpose=inline)

[Building a Multipage Web Application for Customer Churn Prediction in Streamlit Using Python | by Solomon Yeboah | Medium](https://images.openai.com/static-rsc-4/R513ti70G942mGnqGKUdhCtZzBRgE5W05qz_eZ_AajVrXt13FGxf6k2ZlB5e_ARsWbmu83Tk6PLzcz8iZhDTpXZ3GKB5Iz05exC6wxUSkLCs2wISNhmbg5GgEI5NlOCfGEE0VZJ-Rv5XzQOCHNrQc-VQDxaRXc5SBzvZbBn1mRE?purpose=inline)

[The Dashboard | MLAD.ai](https://images.openai.com/static-rsc-4/XC9y0fs_oeOyuVNmub0fL7cuDfsGD2wqn-urXKgSAv8-uNViyt9wRboD8S9tbUQzCCc7MinQTm8ju2LSTXROoMFF1YdyGqtp-KnmrmzQLQCUcMp6S8BZM_5PwsFPOOvybVMJwsgZ-1puk6IIUwBXjqHCMsCE2lfXRpTOgKKoYSI?purpose=inline)

## 6.1 What is Streamlit?

English Definition: Streamlit is an open-source Python framework used to build interactive web applications for data science and machine learning without requiring extensive frontend development.

Hinglish: Streamlit se hum sirf Python code likhkar web applications aur interactive dashboards bana sakte hain. HTML, CSS aur JavaScript ki deep knowledge initially necessary nahi hoti.

Examples:

- Student Performance Predictor.
- Email Spam Detection System.
- AI Study Habit Predictor.
- Sales Analytics Dashboard.
- Machine Learning Model Demo.

## 6.2 Installation

```
pip install streamlit
```

Check version:

```
streamlit --version
```

## 6.3 First Streamlit Application

Create a file:

`app.py`

```
import streamlit as stst.title("My First Streamlit App")st.header("Welcome to Python")st.write("Learning Data Science")st.success("Application is running!")st.info("This is an information message")
```

Run:

```
streamlit run app.py
```

Streamlit automatically opens your application in a browser.

## 6.4 Streamlit Text Functions

```
st.title("Main Title")st.header("Header")st.subheader("Subheader")st.text("Simple Text")st.write("Display different types of data")st.markdown("**Bold Text**")st.caption("Small Caption")st.code("print('Hello World')", language="python")
```

## 6.5 Display Data

```
import streamlit as stimport pandas as pddata = {    "Name": ["Aman", "Riya", "Rahul"],    "Marks": [80, 90, 75]}df = pd.DataFrame(data)st.dataframe(df)st.table(df)st.json({    "name": "Pushpa",    "skill": "Python"})
```

Difference:

- `st.dataframe()` = Interactive table.
- `st.table()` = Static table.
- `st.json()` = JSON viewer.

## 6.6 Streamlit Input Widgets

Text Input

```
name = st.text_input("Enter your name")if name:    st.write("Hello", name)
```

Number Input

```
age = st.number_input(    "Enter your age",    min_value=1,    max_value=100)st.write(age)
```

Slider

```
marks = st.slider(    "Select your marks",    0,    100,    50)st.write("Marks:", marks)
```

Select Box

```
subject = st.selectbox(    "Choose subject",    ["Python", "Java", "C++"])st.write(subject)
```

Radio Button

```
gender = st.radio(    "Select option",    ["Option A", "Option B"])
```

Checkbox

```
agree = st.checkbox("I agree")if agree:    st.write("Thank you!")
```

Button

```
if st.button("Click Me"):    st.success("Button clicked!")
```

Other important widgets:

| Widget       | Function             |
| ------------ | -------------------- |
| Text input   | `st.text_input()`    |
| Text area    | `st.text_area()`     |
| Number input | `st.number_input()`  |
| Slider       | `st.slider()`        |
| Select box   | `st.selectbox()`     |
| Multi-select | `st.multiselect()`   |
| Radio        | `st.radio()`         |
| Checkbox     | `st.checkbox()`      |
| Button       | `st.button()`        |
| Date input   | `st.date_input()`    |
| File upload  | `st.file_uploader()` |
| Color picker | `st.color_picker()`  |

## 6.7 Layout and Sidebar

```
import streamlit as stst.sidebar.title("Navigation")page = st.sidebar.radio(    "Choose Page",    ["Home", "Analytics", "About"])st.title("Dashboard")col1, col2, col3 = st.columns(3)col1.metric("Students", 100)col2.metric("Average Marks", 85)col3.metric("Pass Rate", "95%")
```

Important layout functions:

- `st.sidebar`
- `st.columns()`
- `st.container()`
- `st.tabs()`
- `st.expander()`
- `st.empty()`

## 6.8 Display Charts

```
import streamlit as stimport pandas as pddata = pd.DataFrame({    "Day": ["Mon", "Tue", "Wed", "Thu"],    "Study_Hours": [2, 3, 4, 5]})st.line_chart(    data,    x="Day",    y="Study_Hours")st.bar_chart(    data,    x="Day",    y="Study_Hours")
```

You can also display Matplotlib and Seaborn charts:

```
fig, ax = plt.subplots()ax.plot([1, 2, 3], [10, 20, 30])st.pyplot(fig)
```

## 6.9 File Upload

```
import streamlit as stimport pandas as pduploaded_file = st.file_uploader(    "Upload CSV file",    type=["csv"])if uploaded_file is not None:    df = pd.read_csv(uploaded_file)    st.dataframe(df)    st.write("Dataset Shape:", df.shape)
```

This is especially useful in data analysis projects.

## 6.10 Session State

Definition: Session State allows Streamlit applications to preserve values between reruns during a user's session.

Hinglish: Streamlit interaction hone par script dobara run hoti hai. Session State data ko preserve karne mein help karta hai.

Example:

```
import streamlit as stif "count" not in st.session_state:    st.session_state.count = 0if st.button("Increase"):    st.session_state.count += 1st.write("Count:", st.session_state.count)
```

## 6.11 Caching

Caching helps improve application performance by reusing previously computed results.

`st.cache_data()`

Used for data and computation results.

```
@st.cache_datadef load_data():    return pd.read_csv("students.csv")
```

`st.cache_resource()`

Used for resources such as ML models and database connections.

```
import joblib@st.cache_resourcedef load_model():    return joblib.load("model.joblib")
```

## 6.12 Streamlit Forms

Forms collect multiple inputs and process them when submitted.

```
with st.form("student_form"):    name = st.text_input("Name")    marks = st.number_input(        "Marks",        min_value=0,        max_value=100    )    submitted = st.form_submit_button("Submit")    if submitted:        st.write(name, marks)
```

## 6.13 Streamlit File Download

```
csv = df.to_csv(index=False)st.download_button(    label="Download CSV",    data=csv,    file_name="student_data.csv",    mime="text/csv")
```

## 6.14 Streamlit Project Structure

For professional projects, organize your files:

```
Student-Dashboard/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── students.csv
│
├── models/
│   └── model.joblib
│
├── pages/
│   ├── 1_Analytics.py
│   └── 2_About.py
│
└── assets/
    └── logo.png
```

## 6.15 Deploying Streamlit

Basic deployment workflow:

1. Create your Streamlit application.
2. Test it locally.
3. Create a GitHub repository.
4. Upload your project.
5. Create a Streamlit Community Cloud deployment.
6. Connect the GitHub repository.
7. Select the main file, such as `app.py`.
8. Deploy the application.

Website: [Streamlit Community Cloud](https://streamlit.io/cloud?utm_source=chatgpt.com)

Streamlit interview topics:

- What is Streamlit?
- What is the use of `st.write()`?
- Difference between `st.dataframe()` and `st.table()`.
- What is Session State?
- What is caching?
- Difference between `st.cache_data()` and `st.cache_resource()`?
- How do you deploy a Streamlit application?

# 07. Scikit-learn — Machine Learning Library

[10 Scikit-learn Functions That Simplified My ML Workflow | by Bhagya Rana | Medium](https://images.openai.com/static-rsc-4/1yCOtTytsx5x8AMd8nSExkOjZFpnUMxJCmOTBoy0CtuNApLgGZfYoEm0NMcV_YcSF698hnno6MD_n4wOnHsG-Oopw5y6eC56GYqMeBDSINSRG44TH6Z0WJkqHiruRhE-PQFaFxFH902yuEkmST9TqPmOs3fzp0SeUW5ffIsPoLw?purpose=inline)

[A Simple Example of Pipeline in ML and why do you need to learn it? | by Srinivas Mannem | Medium](https://images.openai.com/static-rsc-4/Nwa0wfIhf9Lvgo46ZUbm2aypnAmxXWGpD5EtUnKam-wI9RJotcWaG_tdJghx8iR0cV81Pb-E8mcFLnW2Ni-0hdFwXS1Gy9RMdUXa-ihnA4CkI_l9ZsO0A6TENdeU-A17IE10RN5kEl9ul8o-3csuyJCGp26aOV8U8qEM_TE6GB8?purpose=inline)

[Machine Learning](https://images.openai.com/static-rsc-4/5dYYjPhvWqEPDofzgfcx4VaiP2NKfsv_J8VsWHD9NXO7XHuQrg6fhB-UsPfYYaT2knLs0mM2ANSXm_xOUWr32osw66jjzKAbQ3YyOe3egvOho8clK9YqqI2Q0e4WmbWutjW_2R9CAPOUuYGWi7YEzXlJWlVS9VRPsi2EvsUAOt8?purpose=inline)

[Python and scikit-learn: Beginner’s Guide to Machine Learning | by shubham mishra | Data Science Collective | Medium](https://images.openai.com/static-rsc-4/VFGgTgtv05GEqr5P7BpoBt-lTB-8hBRB1icwcgyVs3257xMOZ_nY0CLq1JpWMeUd6gLpjEP2BILbSqiqQKcdgoqKJwYr2hUh3IrslCzwBppSVoAoyv4KdhgaNASQZT--SChn46ClmBsUx1DKvwfhoVWZ8-Tn7r4_JdNpjaAMTeg?purpose=inline)

[New Scikit-Learn visual cheat sheet – Hectorv.com](https://images.openai.com/static-rsc-4/D4cmJRInu_jSh9Mwpi0N8ieg4zMDQ5Rem6zcNRtiqS9jwkVF_E99ed1u2-BwnZxqm9ELkpyUy7hIlHb4t3ke3kxniVo-5hkwoK0mNWHsq0X_pORdJplbbn2lDnJVe_kRpwSPzF5BL48GpC0WVHR8G2lnyVS6hyEvkxB1SPVLY_s?purpose=inline)

[什么是 scikit-learn？| NVIDIA 术语表](https://images.openai.com/static-rsc-4/y_HCh-XMbHHRb0GbVvgwk3-z4_2Fs8wFpREkKGxxY1nfgPuhHUY6vD5hnJZFF0yLIQPQIXj5Fcz0Sf6OKKaxc7s8XW3e7y61QP8MKajXnYSoGqXf4VG-UBwUmuC7NSIs9ERxtRYmaRSm8aQKVekxZiZyQdXyE04NJcc4EcXDnTg?purpose=inline)

## 7.1 What is Scikit-learn?

English Definition: Scikit-learn is an open-source Python machine learning library used for data preprocessing, classification, regression, clustering, model selection and model evaluation.

Hinglish: Scikit-learn ek important ML library hai. Iski help se hum data ko preprocess kar sakte hain, machine learning models train kar sakte hain, predictions generate kar sakte hain aur model ki performance check kar sakte hain.

## 7.2 Installation

```
pip install scikit-learn
```

Import:

```
import sklearn
```

## 7.3 Machine Learning Workflow

1\. Collect Dataset

2\. Data Cleaning

3\. Feature Selection

4\. Train-Test Split

5\. Model Training

6\. Model Prediction

7\. Model Evaluation

8\. Model Deployment

## 7.4 Important Types of Machine Learning

1\. Supervised Learning

Model learns from labeled data.

Examples:

- Spam detection.
- Student marks prediction.
- House price prediction.

Two major types:

- Classification: Predicts categories.
- Regression: Predicts numerical values.

2\. Unsupervised Learning

Model discovers patterns from unlabeled data.

Examples:

- Customer segmentation.
- Clustering.
- Anomaly exploration.

3\. Reinforcement Learning

An agent learns through actions, rewards and penalties.

Note: Scikit-learn primarily focuses on classical machine learning rather than deep reinforcement learning.

## 7.5 Train-Test Split

This function divides the dataset into training and testing parts.

```
from sklearn.model_selection import train_test_splitX = df[["Study_Hours", "Sleep_Hours"]]y = df["Marks"]X_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.2,    random_state=42)
```

Explanation:

- `X` = Input features.
- `y` = Target variable.
- `X_train` = Training features.
- `X_test` = Testing features.
- `y_train` = Training targets.
- `y_test` = Testing targets.
- `test_size=0.2` = 20% testing data.
- `random_state=42` = Reproducible split.

## 7.6 Regression Algorithms

Regression predicts continuous numerical values.

Important algorithms:

| Algorithm                   | Purpose                         |
| --------------------------- | ------------------------------- |
| Linear Regression           | Predict numerical values        |
| Polynomial Regression       | Model nonlinear relationships   |
| Decision Tree Regressor     | Tree-based prediction           |
| Random Forest Regressor     | Ensemble learning               |
| Gradient Boosting Regressor | Boosted prediction              |
| Support Vector Regression   | Regression using SVM principles |

### Linear Regression Example

```
from sklearn.linear_model import LinearRegressionmodel = LinearRegression()model.fit(X_train, y_train)predictions = model.predict(X_test)print(predictions)
```

Important methods:

- `fit()` = Train model.
- `predict()` = Generate predictions.
- `score()` = Calculate estimator score.

## 7.7 Classification Algorithms

Classification predicts categories or classes.

| Algorithm              | Example                          |
| ---------------------- | -------------------------------- |
| Logistic Regression    | Spam / Not Spam                  |
| Decision Tree          | Yes / No                         |
| Random Forest          | Fraud classification             |
| Support Vector Machine | Text classification              |
| K-Nearest Neighbors    | Classification by nearby samples |
| Naive Bayes            | Email spam detection             |

Example:

```
from sklearn.ensemble import RandomForestClassifiermodel = RandomForestClassifier(    n_estimators=100,    random_state=42)model.fit(X_train, y_train)predictions = model.predict(X_test)
```

## 7.8 Data Preprocessing

Preprocessing means preparing raw data before training a machine learning model.

A. Missing Value Handling

```
from sklearn.impute import SimpleImputerimputer = SimpleImputer(strategy="mean")X_train = imputer.fit_transform(X_train)X_test = imputer.transform(X_test)
```

Important: Fit preprocessing only on training data, then transform the testing data. This avoids data leakage.

B. Feature Scaling

Feature scaling brings numerical features to comparable scales.

StandardScaler:

```
from sklearn.preprocessing import StandardScalerscaler = StandardScaler()X_train = scaler.fit_transform(X_train)X_test = scaler.transform(X_test)
```

MinMaxScaler:

```
from sklearn.preprocessing import MinMaxScalerscaler = MinMaxScaler()X_train = scaler.fit_transform(X_train)X_test = scaler.transform(X_test)
```

Difference:

| StandardScaler                                | MinMaxScaler                           |
| --------------------------------------------- | -------------------------------------- |
| Centers data around mean 0                    | Usually scales data between 0 and 1    |
| Uses standard deviation                       | Uses minimum and maximum               |
| Useful for many statistical and ML algorithms | Useful when a bounded range is desired |

C. Encoding Categorical Data

Label Encoding:

```
from sklearn.preprocessing import LabelEncoderencoder = LabelEncoder()labels = ["Spam", "Ham", "Spam", "Ham"]encoded = encoder.fit_transform(labels)print(encoded)
```

One-Hot Encoding:

```
from sklearn.preprocessing import OneHotEncoderencoder = OneHotEncoder(    handle_unknown="ignore")encoded = encoder.fit_transform(    [["Python"], ["Java"], ["C++"]])print(encoded.toarray())
```

For input features, one-hot encoding is often preferable to assigning arbitrary numeric labels to unordered categories.

## 7.9 Model Evaluation

A machine learning model must be evaluated after training.

Regression metrics:

| Metric | Meaning                      |
| ------ | ---------------------------- |
| MAE    | Mean Absolute Error          |
| MSE    | Mean Squared Error           |
| RMSE   | Root Mean Squared Error      |
| R²     | Coefficient of determination |

```
from sklearn.metrics import (    mean_absolute_error,    mean_squared_error,    r2_score)print(mean_absolute_error(y_test, predictions))print(mean_squared_error(y_test, predictions))print(r2_score(y_test, predictions))
```

Classification metrics:

| Metric           | Meaning                                                |
| ---------------- | ------------------------------------------------------ |
| Accuracy         | Overall correct predictions                            |
| Precision        | Correct positive predictions among predicted positives |
| Recall           | Correct positive predictions among actual positives    |
| F1-score         | Harmonic mean of precision and recall                  |
| Confusion Matrix | Correct and incorrect predictions by class             |

```
from sklearn.metrics import (    accuracy_score,    precision_score,    recall_score,    f1_score,    confusion_matrix,    classification_report)print("Accuracy:", accuracy_score(y_test, predictions))print("Precision:", precision_score(y_test, predictions))print("Recall:", recall_score(y_test, predictions))print("F1 Score:", f1_score(y_test, predictions))print(confusion_matrix(y_test, predictions))print(classification_report(y_test, predictions))
```

For multiclass classification, select appropriate averaging such as `macro`, `micro` or `weighted` for precision, recall and F1.

## 7.10 Confusion Matrix

[📊 Confusion Matrix Explained (With Python Code & Metrics) | by Soumodeep Santra | Dec, 2025 | Medium](https://images.openai.com/static-rsc-4/xpkaNIzcwRUhd-zBzRfMTywCaCThC8r2-5WDfdG2nC35_h58QSYoD6Wh4IP8cTMcJzOqyrGT8dCN8R1iYpCESXePAGNxajJX-VSyI3Jv4lGhrYNRUTY6_je7QSqKZP0cd1nZvBR-j-1Uu02DNQOtTdvDNhce4xC5gP7QyHcCoYg?purpose=inline)

[medium.com](https://medium.com/%40soumodeepsantra5/confusion-matrix-explained-with-python-code-metrics-f4d78337d3f5?utm_source=chatgpt.com)

Four important terms:

- TP = True Positive.
- TN = True Negative.
- FP = False Positive.
- FN = False Negative.

Example: Email spam detection.

| Actual / Predicted | Spam | Ham |
| ------------------ | ---- | --- |
| Spam               | TP   | FN  |
| Ham                | FP   | TN  |

Understanding confusion matrices is very important for classification projects.

## 7.11 Cross Validation

Cross-validation evaluates a model across multiple train-validation splits.

```
from sklearn.model_selection import cross_val_scorefrom sklearn.ensemble import RandomForestClassifiermodel = RandomForestClassifier(random_state=42)scores = cross_val_score(    model,    X,    y,    cv=5,    scoring="accuracy")print(scores)print(scores.mean())
```

`cv=5` means five-fold cross-validation.

## 7.12 Hyperparameter Tuning

Hyperparameters are settings chosen before model training.

Grid Search:

```
from sklearn.model_selection import GridSearchCVfrom sklearn.ensemble import RandomForestClassifiermodel = RandomForestClassifier(random_state=42)params = {    "n_estimators": [50, 100, 200],    "max_depth": [None, 5, 10]}grid = GridSearchCV(    model,    params,    cv=5,    scoring="accuracy")grid.fit(X_train, y_train)print(grid.best_params_)print(grid.best_score_)
```

Randomized Search:

```
from sklearn.model_selection import RandomizedSearchCV
```

## 7.13 Pipeline

A Pipeline combines preprocessing and model training into one workflow.

```
from sklearn.pipeline import Pipelinefrom sklearn.preprocessing import StandardScalerfrom sklearn.linear_model import LogisticRegressionpipeline = Pipeline([    ("scaler", StandardScaler()),    ("model", LogisticRegression())])pipeline.fit(X_train, y_train)predictions = pipeline.predict(X_test)
```

Benefits:

- Cleaner code.
- Consistent preprocessing.
- Helps prevent data leakage.
- Easier deployment.

## 7.14 Saving and Loading ML Models

Using Joblib:

```
import joblibjoblib.dump(model, "model.joblib")loaded_model = joblib.load("model.joblib")result = loaded_model.predict(X_test)print(result)
```

Important: Only load trusted model files. Serialized files can execute unsafe code during loading.

## 7.15 Important Scikit-learn Modules

| Module                    | Purpose                       |
| ------------------------- | ----------------------------- |
| `sklearn.model_selection` | Data splitting and validation |
| `sklearn.preprocessing`   | Data transformation           |
| `sklearn.impute`          | Missing values                |
| `sklearn.linear_model`    | Linear and logistic models    |
| `sklearn.tree`            | Decision trees                |
| `sklearn.ensemble`        | Random Forest and boosting    |
| `sklearn.svm`             | Support Vector Machines       |
| `sklearn.neighbors`       | KNN                           |
| `sklearn.naive_bayes`     | Naive Bayes                   |
| `sklearn.cluster`         | Clustering                    |
| `sklearn.metrics`         | Model evaluation              |
| `sklearn.pipeline`        | ML pipelines                  |

# 08. How All These Libraries Work Together

This is one of the most important concepts for becoming an AI/ML Engineer.

## Real-world Data Science Workflow

API / CSV / Excel

Collect raw data

Pandas + NumPy

Clean, organize and calculate data

Matplotlib + Seaborn

Explore and visualize data

Scikit-learn

Train and evaluate ML models

Streamlit

Build an interactive ML application

### Example: Student Performance Prediction

| Library      | Work                        |
| ------------ | --------------------------- |
| API          | Collect student information |
| NumPy        | Numerical calculations      |
| Pandas       | Clean student dataset       |
| Matplotlib   | Visualize marks             |
| Seaborn      | Analyze correlations        |
| Scikit-learn | Predict student performance |
| Streamlit    | Build prediction dashboard  |

# 09. Practical Projects for Phase 02

Complete these projects in increasing difficulty.

[Student Performance Analytics | Devpost](https://images.openai.com/static-rsc-4/0AazR-AorcgNatMkYXXbwqNTo1ck1nviV7QQZbz-Dt493jgGtidB6HnS2Y7n_veA8G1CITKrBFsXXNge6GOrjKKrcf6F8LVtqjE1i2RVLSEGDjsm5WelvROAPUdXv4VpxthBWYhbKiZyzHqgwl-uNVucLp3V_WRyjU1tBQeZ-GQ?purpose=inline)

Project 1 — Student Data Analysis

Beginner

- Read CSV using Pandas.
- Calculate average marks.
- Find top-performing students.
- Create graphs using Matplotlib.

[GitHub - Samiya234/Superstore-Dashboard: Dynamic and interactive Superstore Sales Dashboard built with Python and Streamlit. Visualize sales performance across categories, regions, and time periods with advanced filters, treemaps, and time series analysis—designed for actionable business insights. · GitHub](https://images.openai.com/static-rsc-4/nOL5T35BufjR6r3XdUDRew44dQhOjMdzn5eOs0ZEKD-2_cgkObfoZa_7SB1A-6A76WRRMQy9BjaWecKJy6ZmZ5z4NpMJz-dUR0sKEQYY_ypYYIuFG6gqhNd83lWB3rUinjQlbb7cfOQKjFenPfp1QEkOgPUv8H-z7yWYZDzwexs?purpose=inline)

Project 2 — Sales Analytics Dashboard

Beginner–Intermediate

- Clean sales dataset.
- Analyze monthly revenue.
- Create Seaborn heatmaps.
- Visualize sales trends.

[Ashutosh Bhagat](https://images.openai.com/static-rsc-4/l0GaBKibYIHndoUKS4D-3f5CwwuSn9AbWPyMsS4tV1C1h2QNEGXlHHSu5yFz00HXfk8lb4AnvgsR4ZQCS686QmmaFwZC1vYNpohrOl-WzNeeIukdM4Q50Ji67igzVMZTJsBl8UjsdgiRqE5FxW7P1rULVQayX5QPG_aGtlId64g?purpose=inline)

Project 3 — Student Performance Predictor

Intermediate

- Preprocess student data.
- Train Linear Regression.
- Evaluate model performance.
- Create Streamlit interface.

[Easy Weather App: Streamlit + Plotly + Open-Meteo | by Nuno Carvalho | Medium](https://images.openai.com/static-rsc-4/fq4WNUQtBaLUHR9GtiHBl3DK8r8eIjEihaym13u4Z-XPcgkG0y_N8mBMlrG_LezXx2-H6ClCaN4Ra7f-7FExGvEn0Egn31F9skbtVnQwR0IDk8SbeR_PcnqtR1iLAs0i6lwKoTH1Lph0qdaUAZYX0s6fz1yfY_hp93nvWagCbEQ?purpose=inline)

Project 4 — Weather Data Dashboard

Intermediate

- Fetch data using an API.
- Parse JSON.
- Analyze temperature.
- Display interactive charts.

[RSK World - Spam Email Detection | Machine Learning | RSK World - Free Programming Resources & Source Code](https://images.openai.com/static-rsc-4/nXxRlbe67wgQkWGXBq-Qrbpe4H4EoKqVkVQ-lCTz1CTwHyjl69Wad-oMUQ8m7nzT2nM6T2tO5xTvKLVwLWj7HATT00X5fptP5Z4C3ZKyQ72nCGPMMS0TB7PM9CJxfUglQG_ULi1eRkGyp4Op3MkW83-rbu0yembi5kYGBmEpdmI?purpose=inline)

Project 5 — ML Classification Dashboard

Advanced

- Prepare text dataset.
- Train Naive Bayes and Logistic Regression.
- Compare model metrics.
- Build Streamlit prediction interface.

# 10. Important Interview Questions

Prepare these questions after completing the notes.

| No. | Interview question                                |
| --- | ------------------------------------------------- |
| 1   | What is an API?                                   |
| 2   | What is JSON?                                     |
| 3   | Difference between GET and POST?                  |
| 4   | What is NumPy?                                    |
| 5   | Difference between Python List and NumPy Array?   |
| 6   | What is broadcasting?                             |
| 7   | What is a 2D array?                               |
| 8   | What is Pandas?                                   |
| 9   | Difference between Series and DataFrame?          |
| 10  | Difference between loc and iloc?                  |
| 11  | How do you handle missing values?                 |
| 12  | What is GroupBy?                                  |
| 13  | What is data visualization?                       |
| 14  | Difference between Matplotlib and Seaborn?        |
| 15  | What is a heatmap?                                |
| 16  | What is Streamlit?                                |
| 17  | What is Session State?                            |
| 18  | What is Scikit-learn?                             |
| 19  | Difference between classification and regression? |
| 20  | What is train-test split?                         |
| 21  | What is feature scaling?                          |
| 22  | What is overfitting?                              |
| 23  | What is cross-validation?                         |
| 24  | What is a confusion matrix?                       |
| 25  | What is a machine learning pipeline?              |

# 11. Phase 02 — GitHub Folder Structure

Use this structure in your `AIML-Journey` repository.

```
AIML-Journey/
│
└── PHASE_02_Python_for_Data/
    │
    ├── README.md
    │
    ├── 01_API_Handling/
    │   ├── Notes.md
    │   ├── Practice.py
    │   └── Mini_Project/
    │
    ├── 02_NumPy/
    │   ├── Notes.md
    │   ├── Basics.py
    │   ├── Advanced.py
    │   ├── Practice_Questions.py
    │   └── Mini_Project/
    │
    ├── 03_Pandas/
    │   ├── Notes.md
    │   ├── Data_Analysis.py
    │   ├── Data_Cleaning.py
    │   ├── Practice_Questions.py
    │   └── Mini_Project/
    │
    ├── 04_Matplotlib/
    │   ├── Notes.md
    │   ├── Charts.py
    │   └── Mini_Project/
    │
    ├── 05_Seaborn/
    │   ├── Notes.md
    │   ├── Visualizations.py
    │   └── Mini_Project/
    │
    ├── 06_Streamlit/
    │   ├── Notes.md
    │   ├── app.py
    │   └── Mini_Project/
    │
    ├── 07_Scikit_Learn/
    │   ├── Notes.md
    │   ├── Preprocessing.py
    │   ├── Regression.py
    │   ├── Classification.py
    │   ├── Evaluation.py
    │   └── Mini_Project/
    │
    ├── MCQs/
    ├── Interview_Questions/
    └── Reflection.md
```

# 12. Phase 02 Completion Checklist

Your learning progress

# 0%

0 of 21 topics completed

API fundamentals and HTTP methods

GET and POST requests using Python

JSON handling and API error handling

NumPy arrays and dimensions

NumPy indexing, slicing and broadcasting

NumPy statistical and mathematical operations

Pandas Series and DataFrames

Reading CSV, Excel and JSON

Pandas cleaning and missing values

Filtering, sorting and GroupBy

Matplotlib line, bar, scatter and histogram

Matplotlib subplots and customization

Seaborn distributions and categorical plots

Seaborn heatmaps and correlation

Streamlit widgets and layouts

Streamlit Session State and caching

Scikit-learn preprocessing

Regression and classification

Model evaluation and cross-validation

Complete at least two mini projects

GitHub documentation and revision

Reset checklist

## My recommended study strategy

Spend approximately 3–4 weeks on this phase, depending on your daily practice time.

| Week   | Focus                               |
| ------ | ----------------------------------- |
| Week 1 | API + NumPy                         |
| Week 2 | Pandas + Data Cleaning              |
| Week 3 | Matplotlib + Seaborn                |
| Week 4 | Streamlit + Scikit-learn + Projects |

One important rule: Don't just copy code. Har program ko khud type karo, output dekho, dry run karo aur phir usme changes karke practice karo.

Useful official documentation:

- [NumPy Documentation](https://numpy.org/doc/?utm_source=chatgpt.com)
- [Pandas Documentation](https://pandas.pydata.org/docs/?utm_source=chatgpt.com)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html?utm_source=chatgpt.com)
- [Seaborn Documentation](https://seaborn.pydata.org/?utm_source=chatgpt.com)
- [Streamlit Documentation](https://docs.streamlit.io/?utm_source=chatgpt.com)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html?utm_source=chatgpt.com)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/?utm_source=chatgpt.com)

Next learning step: Start with API Handling — Day 1. I can teach one topic at a time with detailed English + Hinglish explanations, code line by line, dry runs, MCQs, assignments and interview questions. I can also prepare a fresh daily lesson and practice assignment every evening.

📚Send daily Phase 02 lessonTap to set up