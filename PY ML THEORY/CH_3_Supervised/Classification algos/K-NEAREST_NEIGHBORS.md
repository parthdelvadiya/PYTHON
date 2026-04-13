# K-Nearest Neighbors (KNN) – Complete Implementation and Interview Guide

---

## 1. What is K-Nearest Neighbors (KNN)?

K-Nearest Neighbors (KNN) is a supervised learning algorithm used for:

- Classification
- Regression

It is a **non-parametric** and **instance-based** algorithm.

Non-parametric → It does not assume any fixed distribution of data.  
Instance-based → It stores the entire training dataset and makes predictions at runtime.

---

## 2. Intuition Behind KNN

KNN works on a simple idea:

"Similar data points exist close to each other."

When a new data point comes:

1. Calculate distance from all training points
2. Select K nearest neighbors
3. Take majority vote (classification)  
   or average value (regression)

---

## 3. Example (Classification)

Problem:

Classify a fruit as Apple or Orange based on weight and color intensity.

If:

K = 3  
Nearest neighbors:

Apple  
Apple  
Orange  

Majority = Apple  

Prediction = Apple

---

## 4. Example (Regression)

Predict house price.

If nearest neighbors have prices:

200000  
220000  
210000  

Prediction = Average = 210000

---

## 5. Distance Metrics

KNN depends heavily on distance calculation.

### Euclidean Distance (Most Common)

Distance = √((x1 - x2)² + (y1 - y2)²)

Used when features are continuous.

---

### Manhattan Distance

Distance = |x1 - x2| + |y1 - y2|

Used when data has grid-like structure.

---

### Minkowski Distance

Generalized distance formula.

Scikit-learn allows different metrics.

---

## 6. Choosing K Value

If K is small (e.g., 1):

- Model sensitive to noise
- High variance
- Overfitting

If K is large:

- Smooth boundary
- High bias
- Underfitting

Choosing optimal K is important.

Usually selected using cross-validation.

---

## 7. Important Notation

| Symbol | Meaning |
|--------|----------|
| X      | Input features |
| y      | Target labels |
| K      | Number of neighbors |
| d      | Distance metric |

Shape requirement:

X → (n_samples, n_features)  
y → (n_samples,)  

---

## 8. Complete Implementation (Classification Example)

Using Breast Cancer Dataset.

```python
# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)


# ==============================
# 6. Predictions
# ==============================
y_pred = model.predict(X_test)

print("\nSample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i]}, Actual: {y_test.iloc[i]}")


# ==============================
# 7. Evaluation Metrics
# ==============================
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)
```

---

## 9. KNN for Regression

To use KNN for regression:

Use:

KNeighborsRegressor

Instead of majority vote, it calculates average of nearest neighbors.

---

## 10. Why Feature Scaling is Important in KNN

KNN is distance-based.

If one feature has large values (e.g., salary in lakhs)  
and another feature has small values (e.g., age),

Large-scale feature dominates distance calculation.

Therefore, always apply:

StandardScaler or MinMaxScaler

Before training KNN.

---

## 11. Time Complexity

Training time:

Very low (just stores data)

Prediction time:

High, because it computes distance to all training samples.

Time complexity during prediction:

O(n)

Where n = number of training samples.

---

## 12. Advantages

- Simple and easy to understand
- No training phase
- Works well with small datasets
- Can handle non-linear decision boundaries

---

## 13. Disadvantages

- Slow prediction for large datasets
- Memory intensive
- Sensitive to irrelevant features
- Sensitive to feature scaling
- Choosing K can be tricky

---

## 14. Important Interview Questions with Strong Explanations

### 1. Is KNN a parametric model?

No.

It does not learn parameters.  
It stores the dataset and makes decisions based on neighbors.

---

### 2. What happens when K = 1?

Model becomes very sensitive to noise.

High variance.  
May overfit.

---

### 3. What happens when K is very large?

Decision boundary becomes smoother.

High bias.  
May underfit.

---

### 4. Why is scaling important in KNN?

Because distance calculation is affected by magnitude of features.

Without scaling, large-value features dominate the model.

---

### 5. Difference between KNN and Logistic Regression?

| KNN | Logistic Regression |
|-----|--------------------|
| Distance-based | Probability-based |
| Lazy learner | Eager learner |
| No training phase | Has training phase |
| Can model complex boundaries | Linear decision boundary |

---

### 6. Can KNN handle multi-class classification?

Yes.

It works naturally with multiple classes using majority voting.

---

### 7. How do you choose best K?

- Use cross-validation  
- Try different values  
- Plot accuracy vs K  
- Choose value with best validation performance  

---

### 8. Does KNN suffer from curse of dimensionality?

Yes.

As number of features increases:

- Distances become less meaningful
- Performance decreases

---

## 15. Decision Boundary Understanding

Small K → Complex boundary  
Large K → Smooth boundary  

K controls bias-variance tradeoff.

---

## Final Interview Summary

K-Nearest Neighbors is a supervised learning algorithm used for classification and regression.

It works by finding K closest training samples using distance metrics and making predictions based on majority vote (classification) or average (regression).

It is simple, non-parametric, and effective for small datasets but computationally expensive for large datasets.

Feature scaling is very important in KNN.

Choosing optimal K is critical to balance bias and variance.