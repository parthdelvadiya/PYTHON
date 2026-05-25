# SimpleImputer in Machine Learning

`SimpleImputer` is used to fill missing values in datasets.

It is part of:

```python id="jlwm1l"
sklearn.impute
```

---

# Why SimpleImputer is Needed

Datasets often contain missing values:

```python id="jlwm2m"
Age     Salary
21      25000
NaN     30000
25      NaN
```

Machine learning models usually cannot handle:

* `NaN`
* missing values

So we replace them using `SimpleImputer`.

---

# Import

```python id="jlwm3n"
from sklearn.impute import SimpleImputer
```

---

# Common Strategies

| Strategy      | Meaning                        |
| ------------- | ------------------------------ |
| mean          | Replace with average           |
| median        | Replace with middle value      |
| most_frequent | Replace with most common value |
| constant      | Replace with fixed value       |

---

# 1. Mean Strategy

Best for:

* numerical data
* normally distributed data

---

# Example

```python id="jlwm4o"
import numpy as np
from sklearn.impute import SimpleImputer

data = np.array([
    [10],
    [20],
    [np.nan],
    [40]
])

imputer = SimpleImputer(strategy='mean')

result = imputer.fit_transform(data)

print(result)
```

---

# Output

```python id="jlwm5p"
[[10.]
 [20.]
 [23.33]
 [40.]]
```

Missing value replaced with mean.

---

# 2. Median Strategy

Best for:

* numerical data
* data with outliers

---

# Example

```python id="jlwm6q"
imputer = SimpleImputer(strategy='median')
```

---

# 3. Most Frequent Strategy

Best for:

* categorical data

---

# Example

```python id="jlwm7r"
import numpy as np
from sklearn.impute import SimpleImputer

data = np.array([
    ['Red'],
    ['Blue'],
    [np.nan],
    ['Red']
])

imputer = SimpleImputer(strategy='most_frequent')

result = imputer.fit_transform(data)

print(result)
```

---

# Output

```python id="jlwm8s"
[['Red']
 ['Blue']
 ['Red']
 ['Red']]
```

Most common value used.

---

# 4. Constant Strategy

Replace missing values with fixed value.

---

# Example

```python id="jlwm9t"
imputer = SimpleImputer(
    strategy='constant',
    fill_value=0
)
```

---

# Important Methods

| Method          | Purpose                  |
| --------------- | ------------------------ |
| fit()           | Learn replacement values |
| transform()     | Replace missing values   |
| fit_transform() | Both together            |

---

# Using Pandas Dataset

```python id="jlwm0u"
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    'Age': [21, 22, None, 25]
})

imputer = SimpleImputer(strategy='mean')

df['Age'] = imputer.fit_transform(df[['Age']])

print(df)
```

---

# Why Median is Sometimes Better

Suppose salaries:

```python id="jlwm1v"
20000
25000
30000
5000000
```

Mean becomes very large because of outlier.

Median works better.

---

# Real Life Example

Suppose student marks are missing.

Possible solutions:

* use class average
* use median marks
* use most common value

SimpleImputer automates this.

---

# Important Note

Always perform imputation:

```python id="jlwm2w"
AFTER train-test split
```

Otherwise:

* data leakage may occur

---

# Correct Workflow

```python id="jlwm3x"
1. Split dataset
2. Fit imputer on training data
3. Transform training data
4. Transform test data
```

---

# Example

```python id="jlwm4y"
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

X_train, X_test = train_test_split(X)

imputer = SimpleImputer(strategy='mean')

X_train = imputer.fit_transform(X_train)

X_test = imputer.transform(X_test)
```

---

# SimpleImputer vs Dropping Rows

| Method        | Meaning                  |
| ------------- | ------------------------ |
| Drop rows     | Remove missing data rows |
| SimpleImputer | Fill missing values      |

---

# When to Use Which

| Situation        | Best Choice   |
| ---------------- | ------------- |
| Few missing rows | Drop rows     |
| Important data   | Use imputer   |
| Numerical data   | Mean/Median   |
| Categorical data | Most frequent |

---

# Interview Definition

```python id="jlwm5z"
SimpleImputer is a preprocessing tool in scikit-learn used to replace missing values using strategies like mean, median, most frequent, or constant values.
```

---

# Final Summary

| Concept       | Meaning                  |
| ------------- | ------------------------ |
| SimpleImputer | Fills missing values     |
| Mean          | Average replacement      |
| Median        | Middle value replacement |
| Most Frequent | Most common value        |
| Constant      | Fixed replacement        |
| Library       | sklearn.impute           |
