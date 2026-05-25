# Cross Validation in Machine Learning

Cross Validation is a technique used to evaluate machine learning models more reliably.

It helps measure:

* model performance
* generalization ability
* overfitting

---

# Why Cross Validation is Needed

Suppose you split dataset once:

```python id="jlwm1a"
Train = 80%
Test = 20%
```

Problem:

* performance depends on random split
* one split may give misleading results

Cross Validation solves this.

---

# Simple Idea

Instead of using:

* one train-test split

Cross Validation uses:

* multiple splits

Model is trained and tested multiple times.

---

# Most Common Type: K-Fold Cross Validation

Dataset is divided into:

```python id="jlwm2b"
K equal parts (folds)
```

Example:

```python id="jlwm3c"
K = 5
```

Dataset split into:

* Fold1
* Fold2
* Fold3
* Fold4
* Fold5

---

# How K-Fold Works

Example with K=5:

| Iteration | Training    | Testing |
| --------- | ----------- | ------- |
| 1         | Fold2-5     | Fold1   |
| 2         | Fold1,3,4,5 | Fold2   |
| 3         | Fold1,2,4,5 | Fold3   |
| 4         | Fold1,2,3,5 | Fold4   |
| 5         | Fold1-4     | Fold5   |

Final score:

* average of all results

---

# Example

Suppose accuracies are:

```python id="jlwm4d"
90%
92%
88%
91%
89%
```

Final accuracy:

```python id="jlwm5e"
(90 + 92 + 88 + 91 + 89) / 5

= 90%
```

---

# Why Cross Validation is Better

Benefits:

* reliable evaluation
* less dependent on random split
* better generalization estimate
* detects overfitting

---

# Import

```python id="jlwm6f"
from sklearn.model_selection import cross_val_score
```

---

# Example

```python id="jlwm7g"
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()

scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print(scores)
print(scores.mean())
```

---

# Output Example

```python id="jlwm8h"
[0.89, 0.91, 0.87, 0.90, 0.88]
```

Average:

```python id="jlwm9i"
0.89
```

---

# Common Types of Cross Validation

| Type              | Meaning                       |
| ----------------- | ----------------------------- |
| K-Fold CV         | Most common                   |
| Stratified K-Fold | Maintains class balance       |
| Leave-One-Out CV  | One sample used for testing   |
| Time Series CV    | Used for sequential/time data |

---

# Stratified K-Fold

Used for classification datasets.

Maintains class proportions.

Example:

```python id="jlwm0j"
90% Normal
10% Fraud
```

Each fold keeps same ratio.

---

# Leave-One-Out Cross Validation (LOOCV)

If dataset has:

```python id="jlwm1k"
100 rows
```

Then:

* 99 rows used for training
* 1 row used for testing

Repeated 100 times.

Very accurate but slow.

---

# Time Series Cross Validation

Used when:

* order of data matters

Example:

* stock prediction
* weather forecasting

Cannot shuffle data randomly.

---

# Cross Validation vs Train-Test Split

| Concept          | Meaning         |
| ---------------- | --------------- |
| Train-Test Split | One split only  |
| Cross Validation | Multiple splits |

---

# Real Life Analogy

Suppose teacher wants fair evaluation.

Instead of:

* one test

Teacher takes:

* multiple tests

Average score gives better understanding.

This is cross validation.

---

# Cross Validation and Hyperparameter Tuning

Cross Validation is heavily used in:

* GridSearchCV
* RandomizedSearchCV

To find best hyperparameters reliably.

---

# Advantages

* Better evaluation
* Uses data efficiently
* Reduces variance
* Detects overfitting

---

# Disadvantages

* Slower training
* Computationally expensive for large datasets

---

# Interview Definition

```python id="jlwm2l"
Cross validation is a model evaluation technique where data is split multiple times into training and testing sets to obtain more reliable performance estimates.
```

---

# Final Summary

| Concept           | Meaning                         |
| ----------------- | ------------------------------- |
| Cross Validation  | Multiple train-test evaluations |
| Main Goal         | Reliable model evaluation       |
| Most Common Type  | K-Fold CV                       |
| Stratified K-Fold | Maintains class balance         |
| Benefit           | Better generalization estimate  |
| Used In           | Hyperparameter tuning           |
