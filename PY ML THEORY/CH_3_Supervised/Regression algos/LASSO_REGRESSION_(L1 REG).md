# L1 Regularization (Lasso Regression) – Complete Implementation and Interview Guide

---

# 1. What is L1 Regularization?

L1 Regularization is a technique used to reduce overfitting in Linear Regression.

It adds a penalty term to the cost function based on the absolute values of coefficients.

Main Goal:

- Reduce overfitting
- Improve generalization
- Automatically perform feature selection

---

# 2. Why Do We Need L1 Regularization?

Suppose we have:

Features:
- Area
- Bedrooms
- Bathrooms
- Owner Phone Number

Clearly, "Owner Phone Number" has no relation to house price.

Normal Linear Regression may still assign some weight to it.

L1 Regularization pushes unimportant feature coefficients toward zero.

Result:

Important Features:
- Area
- Bedrooms

Removed Features:
- Owner Phone Number

---

# 3. Cost Function

Normal Linear Regression Cost Function:

MSE = (1/n) Σ(y - ŷ)²

L1 Regularization adds penalty:

Cost = MSE + λ Σ|w|

Where:

- MSE = Mean Squared Error
- λ (alpha) = Regularization Strength
- w = Model coefficients

Important:

L1 uses absolute values.

|w|

NOT

w²

---

# 4. Why Is It Called Lasso?

LASSO = Least Absolute Shrinkage and Selection Operator

Key Idea:

- Shrink coefficients
- Select important features

Because some coefficients become exactly zero.

---

# 5. Example

Suppose a trained model gives:

Area        = 5.2
Bedrooms    = 2.8
Bathrooms   = 1.1
Garage      = 0.05
ZipCode     = 0.001

After Lasso:

Area        = 5.1
Bedrooms    = 2.7
Bathrooms   = 1.0
Garage      = 0
ZipCode     = 0

Features with coefficient = 0 are effectively removed.

---

# 6. Difference Between Linear Regression and Lasso

Linear Regression:

y = b + w1x1 + w2x2 + ...

Lasso Regression:

y = b + w1x1 + w2x2 + ...

PLUS penalty term during training:

λ Σ|w|

Prediction equation remains same.

Only training process changes.

---

# 7. Understanding Alpha (λ)

Alpha controls regularization strength.

Small Alpha:

alpha = 0.001

Result:

- Almost behaves like Linear Regression
- Little regularization

---

Large Alpha:

alpha = 100

Result:

- Strong regularization
- Many coefficients become zero

---

Example:

Alpha = 0

Coefficients:

[5.4, 2.1, 3.5, 1.2]

Alpha = 50

Coefficients:

[4.9, 1.8, 0, 0]

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
from sklearn.linear_model import Lasso
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
# 4. Train Lasso Model
# ==========================
model = Lasso(alpha=0.1)

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

# 9. Feature Selection Example

Suppose coefficients are:

MedInc      = 0.42
HouseAge    = 0
AveRooms    = 0.08
AveBedrms   = 0
Population  = 0
AveOccup    = -0.02
Latitude    = -0.15
Longitude   = -0.12

Interpretation:

Removed Features:

- HouseAge
- AveBedrms
- Population

Selected Features:

- MedInc
- AveRooms
- AveOccup
- Latitude
- Longitude

---

# 10. Advantages

### 1. Reduces Overfitting

Prevents model from memorizing noise.

---

### 2. Feature Selection

Automatically removes useless features.

---

### 3. Simpler Models

Fewer features.

Easier interpretation.

---

### 4. Handles High-Dimensional Data

Useful when:

Features >> Samples

Example:

1000 features
100 samples

---

# 11. Disadvantages

### 1. Can Remove Useful Features

If alpha is too large.

---

### 2. Not Always Stable

When highly correlated features exist.

May choose one and remove others.

---

### 3. Requires Hyperparameter Tuning

Need to find best alpha value.

---

# 12. Lasso vs Ridge

| Feature | Lasso (L1) | Ridge (L2) |
|----------|------------|------------|
| Penalty | Σ|w| | Σw² |
| Feature Selection | Yes | No |
| Coefficients Become Zero | Yes | Rarely |
| Overfitting Reduction | Yes | Yes |
| Best For | Feature Selection | Multicollinearity |

---

# 13. Lasso vs Linear Regression

| Feature | Linear Regression | Lasso |
|----------|------------------|--------|
| Regularization | No | Yes |
| Feature Selection | No | Yes |
| Overfitting Control | Weak | Strong |
| Complexity | Higher | Lower |

---

# 14. Interview Questions

## 1. What is L1 Regularization?

L1 Regularization adds the absolute value of coefficients as a penalty term to the loss function to reduce overfitting and perform feature selection.

---

## 2. Why is it called Lasso?

LASSO stands for Least Absolute Shrinkage and Selection Operator.

---

## 3. What is the formula of L1 Regularization?

Cost Function:

MSE + λ Σ|w|

---

## 4. What happens when alpha increases?

Higher alpha:

- Stronger regularization
- Smaller coefficients
- More coefficients become zero

---

## 5. Why does Lasso perform feature selection?

Because it can shrink coefficients exactly to zero.

Features with coefficient zero are effectively removed.

---

## 6. Difference Between Ridge and Lasso?

Lasso uses:

Σ|w|

Ridge uses:

Σw²

Lasso can remove features.

Ridge usually keeps all features.

---

## 7. When should we use Lasso?

Use Lasso when:

- Dataset contains many features
- Some features may be irrelevant
- Feature selection is needed
- Overfitting is occurring

---

## 8. What is alpha?

Alpha controls the strength of regularization.

Higher alpha means stronger penalty.

---

# Final Interview Summary

Lasso Regression is Linear Regression with L1 Regularization.

It adds a penalty term:

MSE + λ Σ|w|

The penalty shrinks coefficients and can make some coefficients exactly zero.

This helps reduce overfitting and automatically perform feature selection.

The main hyperparameter is alpha, which controls regularization strength.

Lasso is preferred when we want both prediction and feature selection.