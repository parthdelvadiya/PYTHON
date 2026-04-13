# Logistic Regression – Complete Implementation and Interview Guide

---

## 1. What is Logistic Regression?

Logistic Regression is a supervised learning algorithm used for **classification problems**.

Unlike Linear Regression (which predicts continuous values), Logistic Regression predicts **probabilities** and assigns outputs to **discrete classes**.

It is mainly used for:

- Binary Classification (Yes/No, 0/1, True/False)
- Multi-class Classification (with extension)

---

## 2. Why Not Use Linear Regression for Classification?

If we use Linear Regression for classification:

y = mx + b  

The output can be:

- Less than 0
- Greater than 1

But probabilities must always be between 0 and 1.

To solve this, Logistic Regression uses a **Sigmoid Function** to map values between 0 and 1.

---

## 3. The Sigmoid Function

The sigmoid (logistic) function converts any real value into a probability between 0 and 1.

Formula:

p = 1 / (1 + e^(-z))

Where:

z = b + w1x1 + w2x2 + ... + wnxn  

Properties:

- Output always between 0 and 1  
- S-shaped curve  
- If z is very large → probability close to 1  
- If z is very small → probability close to 0  

---

## 4. Decision Boundary

After computing probability:

If p ≥ 0.5 → Class = 1  
If p < 0.5 → Class = 0  

The threshold (0.5) can be adjusted depending on problem requirements.

Example:

Spam Detection:

If probability of spam = 0.7 → classify as Spam  
If probability of spam = 0.3 → classify as Not Spam  

---

## 5. Mathematical Representation

Step 1: Linear Combination

z = b + w1x1 + w2x2 + ... + wnxn  

Step 2: Apply Sigmoid

p = 1 / (1 + e^(-z))

Step 3: Apply Threshold

Class = 1 if p ≥ 0.5 else 0  

---

## 6. Important Notation

| Symbol | Meaning |
|--------|----------|
| X      | Input features |
| y      | Target (0 or 1) |
| w      | Coefficients (weights) |
| b      | Intercept |
| p      | Predicted probability |

Shape requirement:

X → (n_samples, n_features)  
y → (n_samples,)  

---

## 7. Example Problem (Binary Classification)

Problem:

Predict whether a student will pass (1) or fail (0) based on study hours.

If:

z = -4 + 1.5x  

If student studies 5 hours:

z = -4 + (1.5 × 5)  
z = 3.5  

Apply sigmoid:

p = 1 / (1 + e^(-3.5)) ≈ 0.97  

Probability of passing = 97%  
Prediction = 1 (Pass)

---

## 8. Complete Implementation (Model Code)

Below is complete implementation using Breast Cancer dataset (Binary Classification).

```python
# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ==============================
# 2. Load Dataset
# ==============================
data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("Dataset Preview:\n", df.head())


# ==============================
# 3. Define Features and Target
# ==============================
X = df.drop('target', axis=1)
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
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)


# ==============================
# 6. Model Coefficients
# ==============================
print("\nModel Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


# ==============================
# 7. Predictions
# ==============================
y_pred = model.predict(X_test)

print("\nSample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i]}, Actual: {y_test.iloc[i]}")


# ==============================
# 8. Evaluation Metrics
# ==============================
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)
```

---

## 9. Evaluation Metrics Explained

### Accuracy

Accuracy = Correct Predictions / Total Predictions

Useful when classes are balanced.

---

### Confusion Matrix

|                | Predicted 0 | Predicted 1 |
|----------------|-------------|-------------|
| Actual 0       | True Negative |
| Actual 1       | True Positive |

Helps understand:

- True Positives (TP)
- True Negatives (TN)
- False Positives (FP)
- False Negatives (FN)

---

### Precision

Precision = TP / (TP + FP)

Of all predicted positives, how many are actually positive?

Important in fraud detection.

---

### Recall

Recall = TP / (TP + FN)

Of all actual positives, how many did we correctly identify?

Important in medical diagnosis.

---

### F1 Score

F1 = 2 × (Precision × Recall) / (Precision + Recall)

Used when classes are imbalanced.

---

## 10. Cost Function

Linear Regression uses MSE.

Logistic Regression uses **Log Loss (Binary Cross-Entropy)**.

Why not MSE?

Because:

- Sigmoid makes optimization non-linear
- MSE leads to non-convex loss
- Log Loss provides better convergence

Binary Cross-Entropy:

Loss = -[y log(p) + (1 - y) log(1 - p)]

---

## 11. Assumptions of Logistic Regression

1. Dependent variable is binary  
2. Observations are independent  
3. No strong multicollinearity  
4. Linear relationship between log-odds and features  

Important:

Logistic Regression assumes linearity between features and log-odds, not directly between features and output.

---

## 12. Important Interview Questions with Strong Explanations

### 1. Is Logistic Regression a regression algorithm?

No.

Despite the name, it is used for classification.

---

### 2. Why is it called regression?

Because it models the probability using a linear regression equation inside the sigmoid function.

---

### 3. What is log-odds?

Odds = p / (1 - p)

Log-odds = log(p / (1 - p))

Logistic Regression models log-odds as a linear function of features.

---

### 4. What happens if threshold changes?

Lower threshold → Higher recall, lower precision  
Higher threshold → Higher precision, lower recall  

---

### 5. Can Logistic Regression overfit?

Yes.

Especially when:

- Too many features  
- Small dataset  

Regularization (L1/L2) helps prevent overfitting.

---

### 6. Difference between Linear and Logistic Regression?

| Linear Regression | Logistic Regression |
|------------------|--------------------|
| Predicts continuous values | Predicts probabilities |
| Uses MSE | Uses Log Loss |
| Output range (-∞, +∞) | Output range (0,1) |
| Used for regression | Used for classification |

---

## 13. Multiclass Logistic Regression

Handled using:

- One-vs-Rest (OvR)  
- Multinomial Logistic Regression  

Scikit-learn automatically handles this.

---

## Final Interview Summary

Logistic Regression is a supervised learning algorithm used for classification.

It predicts probability using the sigmoid function:

p = 1 / (1 + e^(-z))

Where z is a linear combination of input features.

It uses Log Loss for optimization and is evaluated using accuracy, precision, recall, F1-score, and confusion matrix.

It is simple, interpretable, and widely used for binary classification problems.