# Support Vector Machine (SVM)

## What is SVM?

SVM (Support Vector Machine) is a supervised machine learning algorithm used for:

* Classification
* Regression
* Outlier Detection

It works by finding the best boundary (hyperplane) between data points.

---

# 1. SVM for Classification

Used to predict categories/classes.

### Examples

* Spam / Not Spam
* Cat / Dog
* Fraud / Not Fraud

### Python Code

```python
from sklearn.svm import SVC

model = SVC()

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

### Important Point

SVM tries to maximize the margin between classes.

---

# 2. SVM for Regression (SVR)

Used to predict continuous numerical values.

### Examples

* House price prediction
* Temperature prediction
* Sales prediction

### Python Code

```python
from sklearn.svm import SVR

model = SVR()

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

### Important Point

SVR tries to fit data within a margin of tolerance instead of predicting every point exactly.

---

# 3. One-Class SVM (Outlier Detection)

Used to detect anomalies/outliers.

### Examples

* Fraud detection
* Intrusion detection
* Defect detection

### Python Code

```python
from sklearn.svm import OneClassSVM

model = OneClassSVM()

model.fit(X_train)

predictions = model.predict(X_test)
```

### Output

* `1`  → Normal
* `-1` → Outlier/Anomaly

### Important Point

One-Class SVM learns the pattern of normal data and identifies unusual points as anomalies.

---

# Feature Scaling in SVM

SVM is very sensitive to feature scales, so scaling is usually required.

## StandardScaler Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

# Quick Revision Table

| Task              | SVM Variant |
| ----------------- | ----------- |
| Classification    | SVC         |
| Regression        | SVR         |
| Outlier Detection | OneClassSVM |

---

# Memory Trick

* `SVC` → Classification
* `SVR` → Regression
* `OneClassSVM` → Outlier Detection