# Decision Tree – Complete Implementation and Interview Guide

---

## 1. What is a Decision Tree?

A Decision Tree is a supervised machine learning algorithm used for:

- Classification
- Regression

It works by splitting data into smaller subsets based on feature values.

The model creates a tree-like structure of decisions.

---

## 2. Intuition Behind Decision Tree

The main idea:

"Ask a series of questions to split the data into pure groups."

Each internal node = Question  
Each branch = Answer  
Each leaf node = Final prediction  

Example:

Is Age > 30?
    Yes → Is Salary > 50k?
            Yes → Approve Loan
            No  → Reject Loan
    No  → Reject Loan

The tree keeps splitting until it reaches pure or nearly pure groups.

Leaf nodes (end nodes)
Contain:
Class counts (e.g., Yes=3, No=1)
✅ Final prediction = majority class

---

## 3. Important Terminology

Root Node  
- First node of the tree

Internal Node  
- A decision node (condition)

Leaf Node  
- Final output (prediction)

Splitting  
- Dividing data based on a condition

Depth  
- Maximum number of splits from root to leaf

---

## 4. How Does Decision Tree Decide Best Split?

It uses impurity measures.

For Classification:

- Gini Index
- Entropy (Information Gain)

For Regression:

- Mean Squared Error (MSE)

---

## 5. Gini Index Formula

Gini = 1 - Σ (pᵢ)²

Where pᵢ = probability of class i.

Lower Gini → More pure node.

---

## 6. Entropy Formula

Entropy = - Σ pᵢ log₂(pᵢ)

Information Gain = Entropy(before split) - Entropy(after split)

Higher Information Gain → Better split.

---

## 7. Example (Classification)

Suppose dataset:

10 samples  
6 Yes  
4 No  

Entropy before split:

Entropy = - (0.6 log₂ 0.6 + 0.4 log₂ 0.4)

Now split by Gender:

Male → 4 Yes, 1 No  
Female → 2 Yes, 3 No  

Calculate entropy for each group and compute Information Gain.

Best split is the one with highest gain.

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
from sklearn.tree import DecisionTreeClassifier
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


# ==============================
# 5. Train Model
# ==============================
model = DecisionTreeClassifier(
    criterion='gini',   # or 'entropy'
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)


# ==============================
# 6. Predictions
# ==============================
y_pred = model.predict(X_test)

print("\nSample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i]}, Actual: {y_test.iloc[i]}")


# ==============================
# 7. Evaluation
# ==============================
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)
```

---

## 9. Decision Tree for Regression

Use:

DecisionTreeRegressor

Instead of impurity, it minimizes:

Mean Squared Error (MSE)

Prediction at leaf node = average of values in that leaf.

---

## 10. Important Hyperparameters

criterion  
- 'gini' or 'entropy'

max_depth  
- Maximum depth of tree

min_samples_split  
- Minimum samples required to split a node

min_samples_leaf  
- Minimum samples required at leaf

max_features  
- Number of features to consider while splitting

---

## 11. Overfitting in Decision Tree

Decision trees can easily overfit.

Why?

Because they keep splitting until data becomes perfectly classified.

Symptoms:
- Very high training accuracy
- Low test accuracy

Solution:
- Limit max_depth
- Increase min_samples_leaf
- Prune tree

---

## 12. Advantages

- Easy to understand and interpret
- No feature scaling required
- Works with numerical and categorical data
- Handles non-linear relationships

---

## 13. Disadvantages

- Prone to overfitting
- Unstable (small data changes can change tree)
- Greedy algorithm (does not guarantee global optimal tree)

---

## 14. Important Interview Questions

### 1. Why Decision Tree does not require feature scaling?

Because it splits based on threshold values, not distance calculations.

---

### 2. What is difference between Gini and Entropy?

Gini:
- Faster computation
- Default in sklearn

Entropy:
- Based on information theory
- Slightly slower

Both measure impurity.

---

### 3. What is pruning?

Removing unnecessary branches to reduce overfitting.

Two types:
- Pre-pruning (limit depth, samples)
- Post-pruning (remove branches after full growth)

---

### 4. Why Decision Tree overfits easily?

Because it tries to perfectly classify training data.

Deep trees memorize data.

---

### 5. What is greedy algorithm in Decision Tree?

At each step, it chooses best local split.

It does not look ahead to check future splits.

---

### 6. Can Decision Tree handle missing values?

Basic sklearn implementation cannot directly handle missing values.

Need preprocessing or advanced tree methods.

---

### 7. Difference Between Decision Tree and KNN?

| Decision Tree | KNN |
|---------------|-----|
| Eager learner | Lazy learner |
| Has training phase | No training phase |
| No scaling required | Scaling required |
| Fast prediction | Slow prediction |

---

## 15. Bias-Variance Understanding

Small depth → High bias, Low variance (Underfitting)  
Large depth → Low bias, High variance (Overfitting)

max_depth controls bias-variance tradeoff.

---

## Final Interview Summary

Decision Tree is a supervised learning algorithm used for classification and regression.

It splits data recursively based on impurity measures such as Gini or Entropy.

It is easy to interpret, does not require scaling, and handles non-linear patterns well.

However, it can easily overfit and requires proper tuning using hyperparameters like max_depth and min_samples_leaf.