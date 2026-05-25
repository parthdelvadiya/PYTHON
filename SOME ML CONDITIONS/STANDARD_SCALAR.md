# StandardScaler in Machine Learning

`StandardScaler` is used to standardize numerical features in a dataset.

It transforms data so that:

* mean becomes 0
* standard deviation becomes 1

It is part of:

```python id="jlwm1a"
sklearn.preprocessing
```

---

# Why StandardScaler is Needed

Different features may have different ranges.

Example:

```python id="jlwm2b"
Age     Salary
20      25000
30      80000
40      150000
```

Problem:

* Salary values are much larger than Age
* Large-scale features dominate the model

StandardScaler fixes this.

---

# What Standardization Does

Formula:

```math id="jlwm3c"
z = (x - μ) / σ
```

Where:

* `x` = original value
* `μ` = mean
* `σ` = standard deviation

---

# Result After Scaling

Before scaling:

```python id="jlwm4d"
Age = [20, 30, 40]
```

After scaling:

```python id="jlwm5e"
[-1.22, 0, 1.22]
```

Mean becomes:

* 0

Standard deviation becomes:

* 1

---

# Import

```python id="jlwm6f"
from sklearn.preprocessing import StandardScaler
```

---

# Basic Example

```python id="jlwm7g"
import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([
    [10],
    [20],
    [30]
])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print(scaled_data)
```

---

# Output

```python id="jlwm8h"
[[-1.22]
 [ 0.00]
 [ 1.22]]
```

---

# Important Methods

| Method          | Purpose            |
| --------------- | ------------------ |
| fit()           | Learn mean and std |
| transform()     | Scale data         |
| fit_transform() | Both together      |

---

# Why Scaling is Important

Some algorithms depend heavily on feature scale.

Without scaling:

* large-value features dominate

With scaling:

* all features contribute equally

---

# Algorithms That Need StandardScaler

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

# Example Without Scaling

Features:

```python id="jlwm9i"
Age = 20
Salary = 200000
```

Distance-based models focus mostly on:

* Salary

Because values are much larger.

---

# Example With Scaling

After scaling:

```python id="jlwm0j"
Age ≈ 0.5
Salary ≈ 0.7
```

Both features contribute fairly.

---

# Using StandardScaler with Train-Test Split

Correct workflow:

```python id="jlwm1k"
1. Split dataset
2. Fit scaler on training data
3. Transform training data
4. Transform test data
```

---

# Correct Example

```python id="jlwm2l"
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test = train_test_split(X)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
```

---

# Why Fit Only on Training Data?

If scaler learns from test data:

* data leakage occurs

Always:

```python id="jlwm3m"
fit -> training data only
```

---

# StandardScaler vs MinMaxScaler

| Feature | StandardScaler | MinMaxScaler |
|---|---|
| Output Range | No fixed range | 0 to 1 |
| Uses Mean/Std | Yes | No |
| Handles Outliers | Better | Sensitive |

---

# Real Life Analogy

Suppose:

* height measured in cm
* salary measured in lakhs

Comparing directly is unfair.

Scaling puts everything on similar scale.

---

# Interview Definition

```python id="jlwm4n"
StandardScaler is a preprocessing technique that standardizes features by removing the mean and scaling data to unit variance.
```

---

# Final Summary

| Concept                          | Meaning                         |
| -------------------------------- | ------------------------------- |
| StandardScaler                   | Standardizes numerical data     |
| Goal                             | Bring features to similar scale |
| Mean After Scaling               | 0                               |
| Standard Deviation After Scaling | 1                               |
| Commonly Used In                 | KNN, SVM, Neural Networks       |
| Avoid Leakage                    | Fit only on training data       |