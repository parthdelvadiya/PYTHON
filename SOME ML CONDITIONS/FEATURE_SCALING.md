# Feature Scaling in Machine Learning

Feature Scaling is a preprocessing technique used to bring all features to a similar scale.

It helps machine learning models perform better and train faster.

---

# Why Feature Scaling is Needed

Different features can have very different ranges.

Example:

```python id="jlwm1a"
Age = 25
Salary = 500000
```

Problem:

* Salary values are much larger
* model gives more importance to Salary

Feature scaling solves this problem.

---

# Goal of Feature Scaling

```python id="jlwm2b"
Make all features contribute equally
```

---

# Example

Before scaling:

```python id="jlwm3c"
Age      Salary
20       20000
30       80000
40       150000
```

After scaling:

```python id="jlwm4d"
Age      Salary
-1.2     -1.1
0        0.2
1.2      0.9
```

Now values are on similar scale.

---

# Why Scaling is Important

Without scaling:

* large-value features dominate
* distance calculations become unfair
* gradient descent becomes slow

With scaling:

* faster convergence
* better performance
* stable training

---

# Algorithms That Need Feature Scaling

| Algorithm           | Scaling Needed? |
| ------------------- | --------------- |
| KNN                 | Yes             |
| K-Means             | Yes             |
| SVM                 | Yes             |
| Logistic Regression | Usually Yes     |
| Neural Networks     | Yes             |

---

# Algorithms That Usually Do NOT Need Scaling

| Algorithm     | Reason      |
| ------------- | ----------- |
| Decision Tree | Uses splits |
| Random Forest | Tree-based  |
| XGBoost       | Tree-based  |

---

# Main Types of Feature Scaling

| Method          | Purpose               |
| --------------- | --------------------- |
| Standardization | Mean = 0, Std = 1     |
| Normalization   | Scale between 0 and 1 |

---

# 1. Standardization

Uses:

```math id="jlwm5e"
z = (x - μ) / σ
```

Where:

* `μ` = mean
* `σ` = standard deviation

Implemented using:

```python id="jlwm6f"
StandardScaler
```

---

# Example

```python id="jlwm7g"
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

# 2. Normalization

Scales values between:

```python id="jlwm8h"
0 and 1
```

Formula:

```math id="jlwm9i"
x' = (x - min) / (max - min)
```

Implemented using:

```python id="jlwm0j"
MinMaxScaler
```

---

# Example

```python id="jlwm1k"
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)
```

---

# Standardization vs Normalization

| Feature | Standardization | Normalization |
|---|---|
| Range | No fixed range | 0 to 1 |
| Outlier Handling | Better | Sensitive |
| Uses Mean/Std | Yes | No |

---

# Real Life Analogy

Suppose:

* height in cm
* salary in lakhs
* weight in kg

Direct comparison is unfair.

Feature scaling converts everything to similar scale.

---

# Feature Scaling and Gradient Descent

Without scaling:

* gradient descent becomes slow
* optimization zig-zags

With scaling:

* faster convergence
* smoother learning

---

# Correct Workflow

```python id="jlwm2l"
1. Split dataset
2. Fit scaler on training data
3. Transform training data
4. Transform test data
```

---

# Correct Example

```python id="jlwm3m"
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test = train_test_split(X)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
```

---

# Important Note

Always:

```python id="jlwm4n"
fit scaler only on training data
```

Otherwise:

* data leakage may occur

---

# Feature Scaling vs Normalization

| Concept         | Meaning                |
| --------------- | ---------------------- |
| Feature Scaling | General process        |
| Standardization | One scaling method     |
| Normalization   | Another scaling method |

---

# Interview Definition

```python id="jlwm5o"
Feature scaling is a preprocessing technique used to bring features to a similar numerical range so that machine learning models perform efficiently and fairly.
```

---

# Final Summary

| Concept         | Meaning                          |
| --------------- | -------------------------------- |
| Feature Scaling | Brings features to similar scale |
| Main Goal       | Fair contribution of features    |
| Standardization | Mean = 0, Std = 1                |
| Normalization   | Values between 0 and 1           |
| Needed In       | KNN, SVM, Neural Networks        |
| Avoid Leakage   | Fit only on training data        |
    