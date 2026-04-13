# Multiple Linear Regression – Complete Implementation and Interview Guide

---

## 1. What is Multiple Linear Regression?

Multiple Linear Regression is a supervised learning algorithm used to predict a continuous numerical value using **more than one independent variable**.

It models the relationship between multiple input features and a single dependent variable by fitting a multidimensional linear equation.

### Real-world Examples

- Predict house price using income, house age, number of rooms  
- Predict salary using experience, education level, skill score  
- Predict sales using marketing spend, season, location  

---

## 2. Mathematical Representation

### Equation

y = b + w1x1 + w2x2 + w3x3 + ... + wnxn

Where:

- y → Dependent variable (target)
- x1, x2, x3 ... xn → Independent variables (features)
- w1, w2, w3 ... wn → Coefficients (weights)
- b → Intercept (bias)

---

### Interpretation

Each coefficient represents the effect of its feature on the target variable **while keeping other features constant**.

Example:

y = 2 + 3x1 + 5x2

- If x1 increases by 1 (keeping x2 constant), y increases by 3.
- If x2 increases by 1 (keeping x1 constant), y increases by 5.
- When all features are 0, y = 2.

This “keeping other variables constant” concept is very important in interviews.

---

## 3. Important Notation

| Symbol | Meaning |
|--------|----------|
| X      | Input data (multiple independent variables) |
| y      | Output data (dependent variable) |

For Multiple Linear Regression:

X → (n_samples, n_features)  
y → (n_samples,)  

Example:

If dataset has 100 samples and 5 features:

X → (100, 5)  
y → (100,)  

Machine learning models always expect:

X → 2D array  
y → 1D array  

---

## 4. Complete Implementation (Model Code)

Below is the complete working implementation using multiple features from the California Housing dataset.

```python
# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==============================
# 2. Load Dataset
# ==============================
data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("Dataset Preview:\n", df.head())


# ==============================
# 3. Define Features and Target (MULTIPLE LINEAR)
# ==============================
X = df.drop('target', axis=1)   # ✅ All features
y = df['target']


# ==============================
# 4. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ==============================
# 5. Train Model
# ==============================
model = LinearRegression()
model.fit(X_train, y_train)


# ==============================
# 6. Model Coefficients
# ==============================
print("\nModel Coefficients (Weights):")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")

print("Intercept (Bias):", model.intercept_)


# ==============================
# 7. Predictions
# ==============================
y_pred = model.predict(X_test)

print("\nSample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i]:.2f}, Actual: {y_test.iloc[i]:.2f}")


# ==============================
# 8. Evaluation Metrics
# ==============================
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation Metrics:")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


# ==============================
# 9. Overfitting Check
# ==============================
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("\nModel Performance:")
print("Training Score:", train_score)
print("Testing Score :", test_score)


# ==============================
# 10. Final Interpretation
# ==============================
if train_score > test_score:
    print("\nModel might be slightly overfitting.")
elif train_score < test_score:
    print("\nModel might be underfitting.")
else:
    print("\nModel is well balanced.")
```

---

## 5. Evaluation Metrics Explained

### MAE (Mean Absolute Error)

Average of absolute errors.

Interpretation:
On average, how much is the model wrong?

---

### MSE (Mean Squared Error)

Average of squared errors.

Why square the errors?

- Removes negative signs  
- Penalizes large errors more  
- Mathematically easier to optimize  

---

### RMSE (Root Mean Squared Error)

Square root of MSE.

Brings error back to original unit of target variable.

---

### R² Score (Coefficient of Determination)

Measures how well independent variables explain the variance in the dependent variable.

| R² Value | Meaning |
|----------|----------|
| 1        | Perfect prediction |
| 0        | Model explains nothing |
| < 0      | Worse than baseline |

If R² = 0.80  
Model explains 80% of variance in target variable.

---

## 6. Overfitting vs Underfitting

Overfitting:

- Training score high  
- Testing score low  
- Model memorizes noise  

Underfitting:

- Training score low  
- Testing score low  
- Model too simple  

Multiple Linear Regression can overfit if:

- Too many features  
- Irrelevant features  
- High multicollinearity  

---

## 7. Important Assumptions of Multiple Linear Regression

1. Linearity between features and target  
2. Independence of errors  
3. Homoscedasticity (constant variance of errors)  
4. No multicollinearity  
5. Normally distributed errors (for statistical inference)

---

## 8. Multicollinearity (Very Important Interview Topic)

Multicollinearity occurs when independent variables are highly correlated with each other.

Problem:

- Coefficients become unstable  
- Hard to interpret feature importance  
- Variance increases  

Detection methods:

- Correlation matrix  
- Variance Inflation Factor (VIF)  

Solution:

- Remove correlated features  
- Use Regularization (Ridge / Lasso)  

---

## 9. Important Interview Questions with Strong Explanations

### 1. What is Multiple Linear Regression?

It is a supervised learning algorithm that models the relationship between multiple independent variables and one dependent variable using a linear equation.

---

### 2. What is the difference between Simple and Multiple Linear Regression?

Simple → One independent variable  
Multiple → More than one independent variable  

Mathematically same concept, but multiple regression operates in higher dimensions.

---

### 3. How do you interpret coefficients?

Each coefficient represents the expected change in the target variable when that feature increases by one unit, keeping other features constant.

---

### 4. What is multicollinearity and why is it a problem?

Multicollinearity occurs when independent variables are highly correlated.

It makes coefficients unstable and reduces interpretability.

---

### 5. How does the model learn?

The model minimizes Mean Squared Error using Ordinary Least Squares method.

It finds optimal weights that minimize total squared error.

---

### 6. Can Multiple Linear Regression overfit?

Yes.

Especially when:

- Number of features is large  
- Dataset is small  
- Features are irrelevant  

---

### 7. What happens if we add useless features?

- Model complexity increases  
- Overfitting risk increases  
- Interpretability decreases  

---

### 8. How do you know if model is good?

Check:

- R² score  
- MAE / RMSE  
- Train vs Test score  
- Residual analysis  

---

## Final Interview Summary

Multiple Linear Regression is a supervised learning algorithm used to predict continuous values using multiple independent variables.

It models the relationship using a linear equation:

y = b + w1x1 + w2x2 + ... + wnxn

Each coefficient represents the effect of a feature while keeping other features constant.

Model performance is evaluated using MAE, MSE, RMSE, and R² score.

Multicollinearity is an important challenge in multiple regression and must be handled carefully.

Train-test split ensures proper generalization and prevents overfitting.