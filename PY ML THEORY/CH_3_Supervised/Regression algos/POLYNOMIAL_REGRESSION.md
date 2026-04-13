# Polynomial Regression – Complete Implementation and Interview Guide

---

## 1. What is Polynomial Regression?

Polynomial Regression is an extension of Linear Regression used to model **non-linear relationships** between the independent variable(s) and the dependent variable.

Even though the relationship between X and y is non-linear, the model is still considered a **linear model** because it is linear in terms of coefficients.

It is used when the data shows a curved pattern instead of a straight-line relationship.

### Real-world Examples

- Predict house price where price increases non-linearly with area  
- Growth rate modeling  
- Demand forecasting with curvature patterns  
- Population growth prediction  

---

## 2. Why Do We Need Polynomial Regression?

Simple Linear Regression fits a straight line:

y = mx + b  

But sometimes the relationship looks like a curve.

Example:

If house price increases slowly at first and then increases rapidly, a straight line will underfit the data.

Polynomial Regression allows us to fit curves like:

y = b + w1x + w2x² + w3x³ + ... + wnxⁿ  

This allows the model to capture non-linear patterns.

---

## 3. Mathematical Representation

### Polynomial Equation (Degree 2 Example)

y = b + w1x + w2x²  

### Degree 3 Example

y = b + w1x + w2x² + w3x³  

Where:

- y → Dependent variable  
- x → Independent variable  
- w1, w2, w3 → Coefficients  
- b → Intercept  
- n → Degree of polynomial  

---

## 4. Important Concept

Polynomial Regression is actually Linear Regression applied to transformed features.

Example:

If original feature is:

X → (x)

After polynomial transformation (degree = 2):

X → (x, x²)

So the model still uses:

LinearRegression()

It just uses more features.

---

## 5. Important Notation

For n samples:

Original feature:

X → (n, 1)  

After Polynomial Transformation (degree = d):

X_poly → (n, d)  

Target:

y → (n,)  

Machine learning models always expect:

X → 2D  
y → 1D  

---

## 6. Complete Implementation (Model Code)

Below is the complete working implementation of Polynomial Regression using one feature (MedInc) from the California Housing dataset.

```python
# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
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
# 3. Define Features and Target
# ==============================
X = df[['MedInc']]   # Using one feature
y = df['target']


# ==============================
# 4. Polynomial Transformation
# ==============================
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)


# ==============================
# 5. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ==============================
# 6. Train Model
# ==============================
model = LinearRegression()
model.fit(X_train, y_train)


# ==============================
# 7. Model Coefficients
# ==============================
print("\nModel Coefficients:", model.coef_)
print("Intercept (Bias):", model.intercept_)


# ==============================
# 8. Predictions
# ==============================
y_pred = model.predict(X_test)

print("\nSample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i]:.2f}, Actual: {y_test.iloc[i]:.2f}")


# ==============================
# 9. Evaluation Metrics
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
# 10. Overfitting Check
# ==============================
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("\nModel Performance:")
print("Training Score:", train_score)
print("Testing Score :", test_score)


# ==============================
# 11. Visualization
# ==============================
import matplotlib.pyplot as plt

# Sort values for smooth curve
sorted_indices = X_test[:, 1].argsort()
X_test_sorted = X_test[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

plt.scatter(X[:, 0], y, label="Actual Data")
plt.plot(X_test_sorted[:, 1], y_pred_sorted, label="Polynomial Curve")
plt.xlabel("Median Income")
plt.ylabel("House Price")
plt.title("Polynomial Regression (Degree 2)")
plt.legend()
plt.show()


# ==============================
# 12. Final Interpretation
# ==============================
if train_score > test_score:
    print("\nModel might be overfitting.")
elif train_score < test_score:
    print("\nModel might be underfitting.")
else:
    print("\nModel is well balanced.")
```

---

## 7. Choosing the Degree

Degree controls model complexity.

If degree = 1 → Simple Linear Regression  
If degree = 2 → Quadratic curve  
If degree = 3 → Cubic curve  

Higher degree:

- More flexible  
- Higher risk of overfitting  

Very high degree:

- Model fits noise  
- Poor generalization  

---

## 8. Overfitting in Polynomial Regression

Polynomial Regression is highly prone to overfitting.

Example:

Degree = 10  

Model may perfectly fit training data but fail on test data.

Always compare:

Training score vs Testing score  

If training score is very high and testing score is much lower → overfitting.

---

## 9. Important Assumptions

Same assumptions as Linear Regression:

1. Linearity in parameters  
2. Independence of errors  
3. Homoscedasticity  
4. No multicollinearity (important when degree is high)  
5. Normally distributed errors (for inference)

---

## 10. Important Interview Questions with Strong Explanations

### 1. Is Polynomial Regression a linear model?

Yes.

Even though it models non-linear relationships, it is linear in terms of coefficients.

Example:

y = b + w1x + w2x²  

This is linear in w1 and w2.

---

### 2. Why not just use high-degree polynomial always?

Because:

- Risk of overfitting  
- Model becomes unstable  
- Poor generalization  

---

### 3. What happens when degree increases?

- Training error decreases  
- Variance increases  
- Risk of overfitting increases  

---

### 4. How does the model learn?

The model uses Ordinary Least Squares to minimize Mean Squared Error after transforming features into polynomial features.

---

### 5. How do you choose the right degree?

- Compare validation scores  
- Use cross-validation  
- Check bias-variance tradeoff  

---

### 6. What is bias-variance tradeoff?

Low degree → High bias, low variance (underfitting)  
High degree → Low bias, high variance (overfitting)  

Goal: Find balance.

---

### 7. What is the difference between Multiple Linear Regression and Polynomial Regression?

Multiple Linear Regression:
Uses multiple independent variables.

Polynomial Regression:
Uses higher powers of the same feature (or combinations) to model non-linear patterns.

---

## Final Interview Summary

Polynomial Regression is an extension of Linear Regression used to model non-linear relationships by transforming features into higher-degree polynomials.

Even though the relationship is non-linear, the model remains linear in terms of coefficients.

The degree controls complexity.

Higher degree increases flexibility but also increases risk of overfitting.

Model performance is evaluated using MAE, MSE, RMSE, and R² score.

Proper train-test split and degree selection are critical to avoid overfitting.