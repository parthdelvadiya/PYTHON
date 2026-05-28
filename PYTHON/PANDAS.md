# Pandas Important Methods with Examples

# What is Pandas?

Pandas is a Python library used for:

* Data Analysis
* Data Cleaning
* Data Manipulation

Import Pandas:

```python id="f1u3xa"
import pandas as pd
```

---

# Creating DataFrame

```python id="g9m2tb"
data = {
    "Name": ["Parth", "Rahul", "Aman"],
    "Age": [20, 21, 22],
    "Marks": [90, 85, 95]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```python id="0lh7ae"
    Name  Age  Marks
0  Parth   20     90
1  Rahul   21     85
2   Aman   22     95
```

---

# Basic Information Methods

---

# head()

Shows first rows.

```python id="8k5krv"
df.head()
```

```python id="j4v28o"
df.head(2)
```

---

# tail()

Shows last rows.

```python id="b9v35w"
df.tail()
```

---

# shape

Returns rows and columns.

```python id="pv14gl"
df.shape
```

Output:

```python id="y7s7s8"
(3, 3)
```

---

# columns

Shows column names.

```python id="9gc6qf"
df.columns
```

---

# dtypes

Shows datatype of columns.

```python id="gt9b2o"
df.dtypes
```

---

# info()

Gives complete summary.

```python id="6l7sfc"
df.info()
```

---

# describe()

Statistical summary.

```python id="o0n3kp"
df.describe()
```

---

# Data Selection

---

# Selecting Single Column

```python id="7vq1d1"
df["Name"]
```

---

# Selecting Multiple Columns

```python id="l0uc3q"
df[["Name", "Marks"]]
```

---

# loc[] → Label Based

```python id="ttm2x3"
df.loc[0]
```

Specific columns:

```python id="v1pq0x"
df.loc[0, "Name"]
```

---

# iloc[] → Index Based

```python id="h8m9rw"
df.iloc[0]
```

```python id="44xt9j"
df.iloc[0, 1]
```

---

# Adding Columns

```python id="1g9wtm"
df["City"] = ["Ahmedabad", "Delhi", "Mumbai"]
```

---

# Updating Values

```python id="wv98mc"
df.loc[0, "Marks"] = 99
```

---

# Deleting Columns

```python id="77g1km"
df.drop("City", axis=1)
```

`axis=1` means column.

---

# Deleting Rows

```python id="k6phg1"
df.drop(0, axis=0)
```

`axis=0` means row.

---

# Sorting

---

# sort_values()

```python id="pb8lhn"
df.sort_values("Marks")
```

Descending:

```python id="fr80o9"
df.sort_values("Marks", ascending=False)
```

---

# Filtering Data

---

# Condition Filtering

```python id="c7mvj0"
df[df["Marks"] > 90]
```

---

# Multiple Conditions

```python id="f8y4hr"
df[(df["Marks"] > 85) & (df["Age"] > 20)]
```

---

# Missing Values

---

# isnull()

Checks null values.

```python id="8p3ifj"
df.isnull()
```

---

# sum()

Count missing values.

```python id="6ldc9k"
df.isnull().sum()
```

---

# dropna()

Removes null rows.

```python id="2m6n4r"
df.dropna()
```

---

# fillna()

Fills missing values.

```python id="4uzmka"
df.fillna(0)
```

---

# Duplicate Handling

---

# duplicated()

Checks duplicates.

```python id="1tahli"
df.duplicated()
```

---

# drop_duplicates()

Removes duplicates.

```python id="ihxj5s"
df.drop_duplicates()
```

---

# Useful Aggregate Functions

---

# mean()

```python id="twg0j0"
df["Marks"].mean()
```

---

# max()

```python id="0yzcx4"
df["Marks"].max()
```

---

# min()

```python id="d6z4e6"
df["Marks"].min()
```

---

# sum()

```python id="tww9rt"
df["Marks"].sum()
```

---

# count()

```python id="0g4w10"
df["Marks"].count()
```

---

# unique()

Unique values.

```python id="a5iv5p"
df["Age"].unique()
```

---

# value_counts()

Counts occurrences.

```python id="9g2mga"
df["Age"].value_counts()
```

---

# GroupBy

Groups similar data.

```python id="gxax9x"
df.groupby("Age")["Marks"].mean()
```

---

# Reading Files

---

# Read CSV

```python id="gjm8zk"
df = pd.read_csv("data.csv")
```

---

# Read Excel

```python id="t55mff"
df = pd.read_excel("data.xlsx")
```

---

# Saving Files

---

# Save CSV

```python id="epkx4g"
df.to_csv("output.csv")
```

---

# Save Excel

```python id="8k83gt"
df.to_excel("output.xlsx")
```

---

# String Operations

---

# str.upper()

```python id="dzvw0j"
df["Name"].str.upper()
```

---

# str.lower()

```python id="u0kr3q"
df["Name"].str.lower()
```

---

# str.contains()

```python id="dx9mnl"
df["Name"].str.contains("a")
```

---

# Apply Function

---

# apply()

Applies custom function.

```python id="hm9pcn"
df["Marks"] = df["Marks"].apply(lambda x: x + 5)
```

---

# Iterating Rows

---

# iterrows()

```python id="ejwjnx"
for index, row in df.iterrows():
    print(row["Name"])
```

---

# Merge DataFrames

```python id="krvz92"
pd.merge(df1, df2, on="ID")
```

---

# Concatenate DataFrames

```python id="dnv3e5"
pd.concat([df1, df2])
```

---

# Rename Columns

```python id="o4o6d6"
df.rename(columns={"Marks": "Score"})
```

---

# Change Datatype

```python id="0n1y3y"
df["Age"] = df["Age"].astype(float)
```

---

# Index Operations

---

# set_index()

```python id="f8fz5g"
df.set_index("Name")
```

---

# reset_index()

```python id="7egqvx"
df.reset_index()
```

---

# Important Interview Notes

| Method     | Purpose            |
| ---------- | ------------------ |
| head()     | First rows         |
| tail()     | Last rows          |
| info()     | Dataset summary    |
| describe() | Statistics         |
| loc[]      | Label selection    |
| iloc[]     | Index selection    |
| groupby()  | Group data         |
| apply()    | Apply function     |
| merge()    | Join tables        |
| concat()   | Combine tables     |
| fillna()   | Fill null values   |
| dropna()   | Remove null values |

---

# Most Common Pandas Workflow

```python id="gwy82t"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

print(df.info())

df.dropna(inplace=True)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df.describe())
```

---