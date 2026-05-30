# Ridge Regression (L2 Regularization) – Complete Implementation and Interview Guide

---

# 1. What is Ridge Regression?

Ridge Regression is a modified version of Linear Regression that uses L2 Regularization to reduce overfitting.

It adds a penalty term based on the square of model coefficients.

Main Goals:

- Reduce overfitting
- Improve generalization
- Handle multicollinearity
- Keep all features while reducing their impact

---

# 2. Why Do We Need Ridge Regression?

Suppose we have:

Features:

- Area
- Bedrooms
- Bathrooms
- Age
- Nearby Schools

A normal Linear Regression model may assign very large weights to some features and start fitting noise.

This leads to:

- High training score
- Poor test score
- Overfitting

Ridge Regression penalizes large coefficients and keeps them small.

---

# 3. Cost Function

Linear Regression:

MSE = (1/n) Σ(y - ŷ)²

Ridge Regression:

Cost = MSE + λ Σw²

Where:

- MSE = Mean Squared Error
- λ (alpha) = Regularization Strength
- w = Model coefficients

Important:

Ridge uses squares of coefficients.

w²

NOT

|w|

---

# 4. Why Is It Called L2 Regularization?

The penalty term uses the square of coefficients:

Σw²

This is known as the L2 Norm.

Hence:

Ridge Regression = L2 Regularization

---

# 5. Example

Suppose Linear Regression produces:

Area        = 12.5
Bedrooms    = 8.3
Bathrooms   = 5.7
Garage      = 4.2

After Ridge:

Area        = 8.1
Bedrooms    = 5.4
Bathrooms   = 3.9
Garage      = 2.7

Notice:

- Coefficients become smaller
- No coefficient becomes exactly zero

---

# 6. Difference Between Linear Regression and Ridge

Linear Regression:

y = b + w1x1 + w2x2 + ...

Ridge Regression:

y = b + w1x1 + w2x2 + ...

PLUS penalty during training:

λ Σw²

Prediction equation remains same.

Only training changes.

---

# 7. Understanding Alpha (λ)

Alpha controls regularization strength.

Small Alpha:

alpha = 0.01

Result:

- Very little regularization
- Behaves like Linear Regression

---

Large Alpha:

alpha = 100

Result:

- Strong regularization
- Coefficients become much smaller

---

Example:

Alpha = 0

Coefficients:

[8.5, 4.3, 7.1]

Alpha = 100

Coefficients:

[2.4, 1.1, 1.9]

---

# 8. Complete Implementation

```python
# ==========================
# 1. Import Libraries
# ==========================
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
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
# 4. Train Ridge Model
# ==========================
model = Ridge(alpha=1.0)

model.fit(X_train, y_train)


# ==========================
# 5. Predictions
# ==========================
y_pred = model.predict(X_test)


# ==========================
# 6. Evaluation Metrics
# ==========================
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

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
train_score = model.score(
    X_train,
    y_train
)

test_score = model.score(
    X_test,
    y_test
)

print("\nTrain Score:", train_score)
print("Test Score :", test_score)
```

---

# 9. Multicollinearity Problem

Multicollinearity occurs when features are highly correlated.

Example:

Features:

- Area in Square Feet
- Area in Square Meters

Both represent the same information.

Linear Regression may produce unstable coefficients.

Example:

Area_ft = 100
Area_m  = -95

This is unstable.

Ridge stabilizes coefficients by shrinking them.

---

# 10. Advantages

### 1. Reduces Overfitting

Prevents extremely large coefficients.

---

### 2. Handles Multicollinearity

One of Ridge's biggest strengths.

---

### 3. More Stable Predictions

Less sensitive to noise.

---

### 4. Keeps All Features

Useful when every feature contains information.

---

# 11. Disadvantages

### 1. No Feature Selection

Coefficients become small but rarely become zero.

---

### 2. Requires Alpha Tuning

Need to find best regularization strength.

---

### 3. Slightly Less Interpretable

Because coefficients are modified.

---

# 12. Ridge vs Lasso

| Feature | Ridge (L2) | Lasso (L1) |
|----------|-----------|-----------|
| Penalty | Σw² | Σ|w| |
| Feature Selection | No | Yes |
| Coefficients Become Zero | Rarely | Often |
| Handles Multicollinearity | Excellent | Good |
| Keeps All Features | Yes | No |

---

# 13. Ridge vs Linear Regression

| Feature | Linear Regression | Ridge |
|----------|------------------|--------|
| Regularization | No | Yes |
| Overfitting Control | Weak | Strong |
| Coefficient Shrinking | No | Yes |
| Multicollinearity Handling | Poor | Excellent |

---

# 14. L1 vs L2 Visualization

Suppose coefficients are:

Linear Regression:

Area       = 10
Bedrooms   = 8
Bathrooms  = 6

Lasso (L1):

Area       = 9
Bedrooms   = 0
Bathrooms  = 5

Ridge (L2):

Area       = 8
Bedrooms   = 6
Bathrooms  = 4

Observation:

- Lasso removes features.
- Ridge keeps features but shrinks them.

---

# 15. Interview Questions

## 1. What is Ridge Regression?

Ridge Regression is Linear Regression with L2 Regularization.

It adds a penalty term based on squared coefficients to reduce overfitting.

---

## 2. What is the formula of Ridge Regression?

Cost Function:

```
MSE + λ Σw²
```

:contentReference[oaicite:0]{index=0}

---

## 3. Why is Ridge called L2 Regularization?

Because the penalty uses squared coefficients:

```
Σw²
```

which is the L2 norm.

---

## 4. What happens when alpha increases?

Higher alpha:

- Stronger regularization
- Smaller coefficients
- Lower variance
- Potentially higher bias

---

## 5. Does Ridge perform feature selection?

No.

Ridge shrinks coefficients but generally does not make them exactly zero.

---

## 6. When should we use Ridge?

Use Ridge when:

- Dataset has many features
- Features are correlated
- Overfitting is occurring
- You want to keep all features

---

## 7. Difference Between Ridge and Lasso?

Ridge:

```
Σw²
```

Lasso:

```
Σ|w|
```

Ridge shrinks coefficients.

Lasso can eliminate coefficients.

---

## 8. What problem does Ridge solve best?

Multicollinearity.

When features are highly correlated, Ridge produces more stable models.

---

# 16. Final Interview Summary

Ridge Regression is Linear Regression with L2 Regularization.

It adds a penalty:

```
MSE + λ Σw²
```

:contentReference[oaicite:1]{index=1}

The penalty discourages large coefficients, reducing overfitting and improving generalization.

Unlike Lasso, Ridge does not perform feature selection because coefficients rarely become exactly zero.

Ridge is particularly useful when features are highly correlated and all features should be retained in the model.