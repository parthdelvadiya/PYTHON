# Simple Linear Regression – Complete Implementation and Interview Guide

---

## 1. What is Linear Regression?

Linear Regression is a supervised learning algorithm used to predict continuous numerical values.

It models the relationship between independent variable(s) and a dependent variable by fitting a straight line.

### Real-world Examples

- Predict house price  
- Predict salary  
- Predict sales  

---

## 2. Types of Linear Regression

### 2.1 Simple Linear Regression

Used when there is only one input feature.

Mathematical Equation:

y = mx + b

Where:

- x → Independent variable (input)  
- y → Dependent variable (output)  
- m → Slope (coefficient / weight)  
- b → Intercept (bias)  

Interpretation:

- The slope (m) represents how much y changes for a one-unit increase in x.  
- The intercept (b) represents the value of y when x = 0.  

Example:

If the equation is:

y = 2x + 5  

When x = 1 → y = 7  
When x = 2 → y = 9  

This means for every 1 unit increase in x, y increases by 2.

---

### 2.2 Multiple Linear Regression

Used when there are multiple input features.

Mathematical Equation:

y = b + w1x1 + w2x2 + ... + wnxn

---

## 3. Important Notation

| Symbol | Meaning |
|--------|----------|
| X      | Input data (independent variables) |
| y      | Output data (dependent variable) |

For Simple Linear Regression (ideal case):

X → (n, 1)  
y → (n,)  

Machine learning models always expect:

X → (n_samples, n_features)  
y → (n_samples,)  

X must always be 2D.  
y must always be 1D.

---

## 4. Complete Implementation (Model Code)

The following is the complete working implementation for Simple Linear Regression using only one feature (MedInc) from the California Housing dataset.

The code is preserved exactly as written.

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
# 3. Define Features and Target (SIMPLE LINEAR)
# ==============================
X = df[['MedInc']]   # ✅ Only ONE feature
y = df['target']


# ==============================
# 4. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(  #20% → Testing 80% → Training
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
print("\nModel Coefficients (Weight):", model.coef_[0]) #m
print("Intercept (Bias):", model.intercept_) #c


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
# 10. Visualization (VERY IMPORTANT)
# ==============================
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, label="Actual Data")
plt.plot(X_test, y_pred, label="Regression Line")
plt.xlabel("Median Income")
plt.ylabel("House Price")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()


# ==============================
# 11. Final Interpretation
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

Average of absolute differences between actual and predicted values.

Interpretation:  
"On average, how much is my model wrong?"

MAE treats all errors equally.

---

### MSE (Mean Squared Error)

Average of squared errors.

Interpretation:  
Take error → square it → take average.

Why square the error?

- Removes negative signs  
- Penalizes large errors more  
- Easier mathematical optimization (differentiable)  

Example:

Model A errors: 2, 2  
Model B errors: 1, 3  

MAE for both = 2  

MSE:  
Model A → (4 + 4)/2 = 4  
Model B → (1 + 9)/2 = 5  

MSE highlights larger mistakes.

---

### RMSE (Root Mean Squared Error)

Square root of MSE.

Interpretation:  
Brings error back to original unit of target variable.  
More interpretable in real-world problems.

---

### R² Score (Coefficient of Determination)

Measures how well the model explains the variance in the data.

| R² Value | Meaning |
|----------|----------|
| 1        | Perfect prediction |
| 0        | Model explains nothing |
| < 0      | Model worse than mean baseline |

Example:

If R² = 0.75  
The model explains 75% of the variance in house prices.

---

## 6. Train-Test Split Explanation

Why do we use train_test_split?

To evaluate model performance on unseen data.

If we train and test on same data:

model.fit(X, y)

The model may show very high accuracy.

But this is fake performance.

Problem: Overfitting  
The model memorizes data instead of learning patterns.

---

What if test_size is too high?

Less training data → weak model.

What if test_size is too low?

Testing becomes unreliable.

---

What is random_state = 42?

Controls randomness of splitting.

Without random_state → every run gives different split.  
With random_state → same split every run.

42 has no special meaning. It is just commonly used.

---

## 7. Overfitting vs Underfitting

Overfitting:

- Training score high  
- Testing score low  
- Model memorizes noise  

Underfitting:

- Training score low  
- Testing score low  
- Model too simple  

In simple linear regression, overfitting is rare.  
More common in complex models.

---

## 8. Important Interview Questions with Strong Explanations

### 1. What is Simple Linear Regression?

Simple Linear Regression is a supervised learning algorithm used to model the relationship between one independent variable and one dependent variable by fitting the best possible straight line.

---

### 2. How does the model learn?

The model learns by minimizing the difference between actual and predicted values using a loss function such as Mean Squared Error.

It finds the optimal slope and intercept that minimize total squared error.

---

### 3. Why do we use MSE instead of MAE?

MSE penalizes larger errors more heavily and is easier to optimize mathematically because it is differentiable.

---

### 4. What is the role of slope?

Slope represents how much the dependent variable changes for a one-unit increase in the independent variable.

If slope = 3  
When income increases by 1 unit → house price increases by 3 units.

---

### 5. What is intercept?

Intercept is the predicted value of the target when input is zero.

Even if zero does not make practical sense, mathematically it is required.

---

### 6. Why must X be 2D?

Models expect:

(n_samples, n_features)

Even with one feature, shape must be:

(n, 1)

That is why we use:

df[['MedInc']]

Instead of:

df['MedInc']

---

### 7. What assumptions does Linear Regression make?

1. Linearity  
2. Independence of errors  
3. Homoscedasticity (constant variance)  
4. No multicollinearity (for multiple regression)  
5. Normally distributed errors (mainly for inference)

---

### 8. Difference between correlation and regression?

Correlation measures strength of relationship.  
Regression models the relationship and predicts values.

---

### 9. How do you know if model is good?

Check:

- R² score  
- MAE / RMSE  
- Train vs Test score comparison  
- Residual analysis  

---

## Final Interview Summary

Simple Linear Regression is a supervised learning algorithm used to model the relationship between one independent variable and one dependent variable using a straight line.

The model learns by minimizing Mean Squared Error.

The slope represents rate of change.  
The intercept represents starting value.

Model performance is evaluated using MAE, MSE, RMSE, and R² score.

Train-test split ensures the model generalizes well to unseen data and prevents overfitting.