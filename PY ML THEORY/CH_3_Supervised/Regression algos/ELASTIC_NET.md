# Elastic Net Regression – Complete Implementation and Interview Guide

---

# 1. What is Elastic Net Regression?

Elastic Net Regression is a regularized version of Linear Regression that combines:

- L1 Regularization (Lasso)
- L2 Regularization (Ridge)

Main Goals:

- Reduce Overfitting
- Handle Multicollinearity
- Perform Feature Selection
- Keep model stable

Elastic Net gives the benefits of both Ridge and Lasso.

---

# 2. Why Do We Need Elastic Net?

Suppose we have:

Features:

- Area
- Bedrooms
- Bathrooms
- Age
- Distance to City
- Owner ID

Problems:

1. Some features are useless
2. Some features are highly correlated
3. Model is overfitting

Lasso solves feature selection.

Ridge solves multicollinearity.

Elastic Net solves both.

---

# 3. Cost Function

Linear Regression:

MSE

Elastic Net:

Cost = MSE + λ₁Σ|w| + λ₂Σw²

Where:

- MSE = Mean Squared Error
- λ₁ = L1 Penalty
- λ₂ = L2 Penalty
- w = Coefficients

Elastic Net applies:

- Absolute penalty (L1)
- Squared penalty (L2)

at the same time.

---

# 4. Intuition

Lasso says:

"Remove useless features."

Ridge says:

"Keep all features but reduce their influence."

Elastic Net says:

"Remove some features and shrink the rest."

---

# 5. Example

Linear Regression:

Area        = 12
Bedrooms    = 8
Bathrooms   = 5
Garage      = 2
ZipCode     = 1

Lasso:

Area        = 10
Bedrooms    = 6
Bathrooms   = 4
Garage      = 0
ZipCode     = 0

Ridge:

Area        = 8
Bedrooms    = 5
Bathrooms   = 3
Garage      = 1
ZipCode     = 0.5

Elastic Net:

Area        = 9
Bedrooms    = 5
Bathrooms   = 3
Garage      = 0
ZipCode     = 0.2

Observation:

- Some coefficients become zero
- Remaining coefficients are shrunk

---

# 6. Important Hyperparameters

Elastic Net has two important parameters.

---

## Alpha

Controls overall regularization strength.

Example:

alpha = 0.001

Weak Regularization

alpha = 100

Strong Regularization

---

## l1_ratio

Controls balance between L1 and L2.

Range:

0 → 1

Meaning:

l1_ratio = 0

Pure Ridge

---

l1_ratio = 1

Pure Lasso

---

l1_ratio = 0.5

50% Lasso
50% Ridge

---

Examples:

l1_ratio = 0.2

Mostly Ridge

---

l1_ratio = 0.8

Mostly Lasso

---

# 7. Complete Implementation

```python
# ==========================
# 1. Import Libraries
# ==========================
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# ==========================
# 2. Load Dataset
# ==========================
data = fetch_california_housing()

X = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

y = data.target


# ==========================
# 3. Train-Test Split
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================
# 4. Train Elastic Net
# ==========================
model = ElasticNet(
    alpha=0.1,
    l1_ratio=0.5
)

model.fit(X_train, y_train)


# ==========================
# 5. Predictions
# ==========================
y_pred = model.predict(X_test)


# ==========================
# 6. Metrics
# ==========================
mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test,
    y_pred
)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R²  :", r2)


# ==========================
# 7. Coefficients
# ==========================
print("\nCoefficients:")

for feature, coef in zip(
    X.columns,
    model.coef_
):
    print(feature, ":", coef)


# ==========================
# 8. Train/Test Score
# ==========================
print(
    "\nTrain Score:",
    model.score(X_train, y_train)
)

print(
    "Test Score:",
    model.score(X_test, y_test)
)
```

---

# 8. Feature Selection Example

Suppose coefficients are:

MedInc      = 0.50
HouseAge    = 0.03
AveRooms    = 0.08
AveBedrms   = 0
Population  = 0
AveOccup    = -0.02
Latitude    = -0.15
Longitude   = -0.12

Interpretation:

Removed Features:

- AveBedrms
- Population

Retained Features:

- MedInc
- HouseAge
- AveRooms
- AveOccup
- Latitude
- Longitude

---

# 9. Advantages

## 1. Reduces Overfitting

Controls model complexity.

---

## 2. Feature Selection

Can remove irrelevant features.

---

## 3. Handles Multicollinearity

Works well with correlated features.

---

## 4. More Stable Than Lasso

Especially when features are highly correlated.

---

## 5. Works Well on High-Dimensional Data

Useful when:

Features > Samples

---

# 10. Disadvantages

## 1. More Hyperparameters

Need to tune:

- alpha
- l1_ratio

---

## 2. Slightly More Complex

Compared to Ridge or Lasso.

---

## 3. Requires Feature Scaling

Always scale data before using Elastic Net.

Example:

```python
from sklearn.preprocessing import StandardScaler
```

---

# 11. Elastic Net vs Lasso vs Ridge

| Feature | Ridge | Lasso | Elastic Net |
|----------|--------|--------|------------|
| L1 Penalty | ❌ | ✅ | ✅ |
| L2 Penalty | ✅ | ❌ | ✅ |
| Feature Selection | ❌ | ✅ | ✅ |
| Handles Multicollinearity | ✅ | Good | ✅ |
| Stability | High | Medium | High |

---

# 12. When Should We Use Each?

Use Ridge When:

- All features are important
- Multicollinearity exists

---

Use Lasso When:

- Many useless features
- Feature selection needed

---

Use Elastic Net When:

- Many features
- Correlated features
- Need feature selection
- Want stable model

---

# 13. Interview Questions

## 1. What is Elastic Net Regression?

Elastic Net is a Linear Regression model that combines L1 and L2 Regularization.

---

## 2. What is the Cost Function?

Cost Function:

MSE + λ₁Σ|w| + λ₂Σw²

---

## 3. Why use Elastic Net instead of Lasso?

Lasso may become unstable when features are highly correlated.

Elastic Net handles correlated features better.

---

## 4. What does l1_ratio do?

It controls the balance between:

- L1 Regularization
- L2 Regularization

---

## 5. What happens when l1_ratio = 0?

Elastic Net becomes Ridge Regression.

---

## 6. What happens when l1_ratio = 1?

Elastic Net becomes Lasso Regression.

---

## 7. Does Elastic Net perform feature selection?

Yes.

Some coefficients can become zero.

---

## 8. Does Elastic Net handle multicollinearity?

Yes.

This is one of its biggest advantages.

---

# 14. Common Interview Comparison

Question:

"When would you choose Ridge, Lasso, or Elastic Net?"

Answer:

Ridge:
- Use when all features are important.
- Best for multicollinearity.

Lasso:
- Use when feature selection is required.

Elastic Net:
- Use when dataset has many features and correlated variables.
- Provides both feature selection and coefficient shrinking.

---

# Final Interview Summary

Elastic Net Regression combines the strengths of Ridge (L2) and Lasso (L1).

Cost Function:

MSE + λ₁Σ|w| + λ₂Σw²

It reduces overfitting, handles multicollinearity, and performs feature selection.

The two main hyperparameters are:

- alpha → regularization strength
- l1_ratio → balance between L1 and L2

Elastic Net is often preferred when working with large datasets containing many correlated features because it provides a balance between stability and feature selection.