# Regularization in Machine Learning

Regularization is a technique used to reduce overfitting in machine learning models.

Overfitting means:

* Model learns training data too perfectly
* Learns noise and random patterns
* Performs poorly on unseen data

Regularization helps by:

* Reducing model complexity
* Penalizing large weights
* Improving generalization

---

# Why Regularization is Needed

Suppose a model learns:

```python
y = 2*x1 + 5*x2 - 1000*x3 + 0.0001*x4
```

Very large coefficients make the model unstable.

Small changes in input can create huge output changes.

Regularization controls these weights.

---

# Types of Regularization

| Type     | Name             | Penalty                |
| -------- | ---------------- | ---------------------- |
| L1       | Lasso Regression | Sum of absolute values |
| L2       | Ridge Regression | Sum of squared values  |
| Combined | ElasticNet       | L1 + L2                |

---

# Cost Function Without Regularization

```math
J(θ) = (1/n) Σ(yᵢ - ŷᵢ)²
```

Model only minimizes prediction error.

---

# Ridge Regression (L2 Regularization)

Ridge adds squared penalty.

## Formula

```math
J(θ) = (1/n) Σ(yᵢ - ŷᵢ)² + λ Σθⱼ²
```

---

# What Ridge Does

Suppose coefficients are:

```python
[100, 200, 300]
```

Penalty becomes:

```python
100^2 + 200^2 + 300^2
```

Large values become expensive.

Model reduces them:

```python
[10, 20, 30]
```

---

# Important Property of Ridge

Ridge:

* Reduces coefficients
* Does NOT make coefficients exactly zero

Example:

Before Ridge:

```python
[5.6, 8.9, 0.3, 100]
```

After Ridge:

```python
[4.8, 6.7, 0.1, 40]
```

---

# When Ridge Regression is Used

Use Ridge when:

* Most features are important
* Features are correlated
* Multicollinearity exists

Example:

* height_cm
* height_meter
* height_inch

These contain similar information.

Ridge stabilizes the model.

---

# Ridge Regression Example

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# Create dataset
X, y = make_regression(
    n_samples=100,
    n_features=5,
    noise=20,
    random_state=42
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = Ridge(alpha=1.0)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Coefficients
print(model.coef_)
```

---

# Lasso Regression (L1 Regularization)

Lasso adds absolute value penalty.

## Formula

```math
J(θ) = (1/n) Σ(yᵢ - ŷᵢ)² + λ Σ|θⱼ|
```

---

# What Lasso Does

Suppose coefficients are:

```python
[5, 10, 0.2, 50]
```

After Lasso:

```python
[4, 0, 0, 30]
```

Some coefficients become exactly zero.

That means:

* Feature removed
* Feature selection performed

---

# Important Property of Lasso

Lasso automatically removes useless features.

This is called:

* Feature Selection

---

# When Lasso is Used

Use Lasso when:

* Dataset has many useless features
* Feature selection is needed
* High-dimensional data exists

Examples:

* NLP
* Text classification
* Spam detection
* Gene prediction

---

# Lasso Regression Example

```python
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# Create dataset
X, y = make_regression(
    n_samples=100,
    n_features=10,
    noise=20,
    random_state=42
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = Lasso(alpha=0.1)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Coefficients
print(model.coef_)
```

---

# Example Output of Lasso

```python
[12.5, 0, 0, 8.2, 0, 15.1]
```

Features with coefficient 0 are removed.

---

# Difference Between Ridge and Lasso

| Feature                  | Ridge               | Lasso           |
| ------------------------ | ------------------- | --------------- |
| Penalty                  | Square              | Absolute        |
| Feature Selection        | No                  | Yes             |
| Coefficients Become Zero | No                  | Yes             |
| Best For                 | Correlated features | Sparse datasets |

---

# Understanding Lambda (λ)

Lambda controls regularization strength.

## Small Lambda

```python
alpha = 0.001
```

* Small penalty
* Model behaves like normal regression

---

## Large Lambda

```python
alpha = 1000
```

* Huge penalty
* Weights become very small
* May cause underfitting

---

# ElasticNet Regression

ElasticNet combines:

* Ridge
* Lasso

## Formula

```math
J(θ) = (1/n) Σ(yᵢ - ŷᵢ)² + λ₁Σ|θ| + λ₂Σθ²
```

---

# ElasticNet Example

```python
from sklearn.linear_model import ElasticNet

model = ElasticNet(
    alpha=1.0,
    l1_ratio=0.5
)

model.fit(X_train, y_train)
```

---

# Regularization in Deep Learning

Regularization is also used in neural networks.

Methods:

* L1/L2 Regularization
* Dropout
* Early Stopping
* Data Augmentation

---

# Example of Overfitting

Without Regularization:

```python
Train Accuracy = 99%
Test Accuracy = 55%
```

With Regularization:

```python
Train Accuracy = 91%
Test Accuracy = 89%
```

---

# Real Life Analogy

Without regularization:

* Student memorizes answers

With regularization:

* Student understands concepts

Regularization forces models to learn general patterns instead of memorizing.

---

# Interview Questions

## Why Ridge Uses Squares?

Because:

* Smooth optimization
* Strongly penalizes large coefficients

---

## Why Lasso Produces Zero Coefficients?

Because absolute value optimization can shrink some weights completely to zero.

---

## Can We Combine Ridge and Lasso?

Yes.

That is called:

* ElasticNet

---

# Final Summary

| Concept        | Meaning                    |
| -------------- | -------------------------- |
| Regularization | Reduces overfitting        |
| Ridge          | Shrinks coefficients       |
| Lasso          | Shrinks + removes features |
| ElasticNet     | Combination of both        |
| Lambda         | Controls penalty strength  |
| Goal           | Better generalization      |