# Hyperparameter Tuning

Hyperparameter Tuning is the process of finding the best hyperparameter values for a machine learning model.

It helps improve:

* accuracy
* performance
* generalization

---

# What are Hyperparameters?

Hyperparameters are settings decided before training.

Examples:

```python id="jlwm1a"
learning_rate
n_estimators
max_depth
k
batch_size
epochs
```

They are NOT learned by the model.

---

# Parameters vs Hyperparameters

| Concept         | Meaning                 |
| --------------- | ----------------------- |
| Parameters      | Learned during training |
| Hyperparameters | Set before training     |

---

# Example

Linear Regression:

```python id="jlwm2b"
y = wx + b
```

Here:

* `w` and `b` are parameters

---

Decision Tree:

```python id="jlwm3c"
max_depth = 5
```

`max_depth` is hyperparameter.

---

# Why Hyperparameter Tuning is Needed

Wrong hyperparameters can cause:

* underfitting
* overfitting
* poor accuracy

Good hyperparameters improve model performance.

---

# Example

## Small Decision Tree

```python id="jlwm4d"
max_depth = 1
```

Model becomes too simple.

High bias.

---

## Very Large Tree

```python id="jlwm5e"
max_depth = 100
```

Model memorizes data.

High variance.

---

# Goal of Hyperparameter Tuning

```python id="jlwm6f"
Find best balance between bias and variance
```

---

# Common Hyperparameters

| Model             | Important Hyperparameters |
| ----------------- | ------------------------- |
| Linear Regression | alpha                     |
| Decision Tree     | max_depth                 |
| Random Forest     | n_estimators              |
| KNN               | k                         |
| Neural Network    | learning_rate, epochs     |
| SVM               | C, kernel                 |

---

# Methods of Hyperparameter Tuning

| Method                | Meaning                 |
| --------------------- | ----------------------- |
| Manual Search         | Try values manually     |
| Grid Search           | Try all combinations    |
| Random Search         | Try random combinations |
| Bayesian Optimization | Smart search method     |

---

# 1. Manual Search

Try values manually.

Example:

```python id="jlwm7g"
k = 3
k = 5
k = 7
```

Simple but slow.

---

# 2. Grid Search

Tests all combinations.

---

# Example

```python id="jlwm8h"
max_depth = [3, 5]
n_estimators = [100, 200]
```

Combinations:

```python id="jlwm9i"
(3,100)
(3,200)
(5,100)
(5,200)
```

Best combination selected automatically.

---

# GridSearchCV Example

```python id="jlwm0j"
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

params = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5]
}

grid = GridSearchCV(
    model,
    params,
    cv=5
)

grid.fit(X_train, y_train)

print(grid.best_params_)
```

---

# 3. Random Search

Randomly tests combinations.

Faster than Grid Search for large search spaces.

---

# Example

```python id="jlwm1k"
from sklearn.model_selection import RandomizedSearchCV
```

---

# Why Cross Validation is Used

GridSearchCV uses:

* Cross Validation (CV)

This gives:

* more reliable evaluation
* better generalization

---

# Real Life Analogy

Suppose making coffee.

Hyperparameters:

* sugar amount
* milk amount
* coffee amount

You try different combinations to get best taste.

This is hyperparameter tuning.

---

# Hyperparameter Tuning in Deep Learning

Important hyperparameters:

| Hyperparameter | Purpose         |
| -------------- | --------------- |
| Learning Rate  | Step size       |
| Batch Size     | Data per update |
| Epochs         | Training cycles |
| Dropout Rate   | Regularization  |

---

# Example

Bad learning rate:

```python id="jlwm2l"
lr = 100
```

Training becomes unstable.

---

Good learning rate:

```python id="jlwm3m"
lr = 0.001
```

Stable learning.

---

# Hyperparameter Tuning vs Training

| Concept               | Meaning            |
| --------------------- | ------------------ |
| Training              | Learn parameters   |
| Hyperparameter Tuning | Find best settings |

---

# Common Problems

| Problem       | Cause                       |
| ------------- | --------------------------- |
| Underfitting  | Hyperparameters too simple  |
| Overfitting   | Hyperparameters too complex |
| Slow Training | Large search space          |

---

# Best Practice

* Start simple
* Use Random Search first
* Use Grid Search for smaller spaces
* Use validation data

---

# Interview Definition

```python id="jlwm4n"
Hyperparameter tuning is the process of finding the optimal hyperparameter values that maximize machine learning model performance.
```

---

# Final Summary

| Concept          | Meaning                            |
| ---------------- | ---------------------------------- |
| Hyperparameter   | Predefined model setting           |
| Goal             | Improve performance                |
| Grid Search      | Try all combinations               |
| Random Search    | Try random combinations            |
| Cross Validation | Reliable evaluation                |
| Result           | Better accuracy and generalization |
