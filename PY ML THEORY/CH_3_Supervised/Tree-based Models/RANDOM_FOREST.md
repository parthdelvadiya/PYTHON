# Random Forest – Complete Implementation and Interview Guide

---

## 1. What is Random Forest?

Random Forest is a supervised machine learning algorithm used for:

- Classification
- Regression

It is an ensemble learning method that builds multiple Decision Trees and combines their outputs.

Final prediction:
- Classification → Majority Voting
- Regression → Average of predictions

---

## 2. Why Random Forest?

Decision Trees are powerful but prone to overfitting.

Random Forest solves this by:
- Training multiple trees
- Using random subsets of data
- Using random subsets of features
- Combining results

This reduces variance and improves generalization.

---

## 3. Core Idea Behind Random Forest

Two main concepts:

### 1. Bagging (Bootstrap Aggregation)

- Random samples are taken from dataset (with replacement).
- Each tree is trained on different random data.

Example:
If dataset has 100 rows,
Each tree may train on different 100 rows (some repeated, some missing).

---

### 2. Random Feature Selection

At each split:
- Instead of checking all features,
- Random subset of features is considered.

This makes trees less correlated.

---

## 4. Why Random Forest Works Better?

Single Decision Tree:
- High variance
- Easily overfits

Random Forest:
- Reduces variance
- More stable
- Better test accuracy

Because:
Average of multiple overfitting trees → reduces overall overfitting.

---

## 5. Complete Implementation (Classification Example)

Using Breast Cancer Dataset.

```python
# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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
model = RandomForestClassifier(
    n_estimators=100,      # number of trees
    criterion='gini',      # impurity measure
    max_depth=None,        # full growth
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

## 6. Random Forest for Regression

Use:

RandomForestRegressor

Final prediction:
Average of all tree predictions.

Loss function:
Minimizes Mean Squared Error (MSE).

---

## 7. Important Hyperparameters

n_estimators  
- Number of trees in forest  
- More trees → better performance but slower

max_depth  
- Maximum depth of each tree

min_samples_split  
- Minimum samples required to split

min_samples_leaf  
- Minimum samples required at leaf

max_features  
- Number of features to consider at each split  
- 'sqrt' (default for classification)  
- 'log2'  
- or integer value

bootstrap  
- Whether to use sampling with replacement

---

## 8. Feature Importance

Random Forest provides feature importance automatically.

Example:

```python
importances = model.feature_importances_

for name, score in zip(X.columns, importances):
    print(name, score)
```

Higher value → more important feature.

This is useful in real-world feature selection.

---

## 9. Advantages

- Reduces overfitting
- High accuracy
- Handles large datasets well
- Works with high dimensional data
- Handles non-linear relationships
- No feature scaling required

---

## 10. Disadvantages

- Slower than single decision tree
- Less interpretable
- Large memory usage
- Not good for real-time low-latency systems

---

## 11. Overfitting in Random Forest

Random Forest is much less likely to overfit than Decision Tree.

But:
If trees are very deep and n_estimators is small → can still overfit.

Solution:
- Increase n_estimators
- Limit max_depth
- Tune min_samples_leaf

---

## 12. Bias-Variance Tradeoff

Decision Tree:
Low bias, High variance

Random Forest:
Slightly higher bias,
Much lower variance

Overall better generalization.

---

## 13. Important Interview Questions

### 1. Why Random Forest performs better than Decision Tree?

Because it reduces variance by averaging multiple trees trained on different subsets of data.

---

### 2. What is difference between Bagging and Boosting?

Bagging:
- Trees trained independently
- Parallel training
- Reduces variance

Boosting:
- Trees trained sequentially
- Each tree corrects previous errors
- Reduces bias

Random Forest uses Bagging.

---

### 3. Why Random Forest does not require scaling?

Because it is based on tree splits, not distance calculation.

---

### 4. What happens if n_estimators increases?

- Accuracy improves (up to a limit)
- Training time increases
- Variance decreases

---

### 5. What is Out-of-Bag (OOB) Score?

Since each tree is trained on bootstrap data,
some samples are not used.

These unused samples are called Out-of-Bag samples.

They can be used to estimate model performance without separate validation set.

Enable using:

oob_score=True

---

### 6. Can Random Forest handle missing values?

Sklearn version does not directly handle missing values.
Need preprocessing.

---

### 7. Why Random Feature Selection is important?

If all trees use same best feature always,
trees become similar.

Random feature selection makes trees diverse.

Diverse trees → Better averaging → Better generalization.

---

## 14. Example to Explain in Interview

If one tree predicts:
Class A

Another predicts:
Class B

Another predicts:
Class A

Final output:
Class A (majority voting)

For regression:
Tree outputs:
100, 110, 90

Final prediction:
(100 + 110 + 90) / 3 = 100

---

## Final Interview Summary

Random Forest is an ensemble learning algorithm that builds multiple decision trees using bootstrap sampling and random feature selection.

It reduces variance, improves generalization, and performs better than a single decision tree.

It is widely used because it provides high accuracy, handles non-linear relationships, and works well without heavy preprocessing.