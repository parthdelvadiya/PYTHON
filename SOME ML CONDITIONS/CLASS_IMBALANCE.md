# Class Imbalance in Machine Learning

Class Imbalance occurs when one class has significantly more samples than another class.

Because of this:

* Model becomes biased toward majority class
* Minority class predictions become poor
* Accuracy can become misleading

---

# Simple Example

Suppose a dataset contains:

```python
950 = Not Fraud
50  = Fraud
```

Total:

```python
1000 records
```

Distribution:

```python
95% Not Fraud
5% Fraud
```

This is a class imbalance problem.

---

# Why It Is Dangerous

Suppose model predicts:

```python
Not Fraud
Not Fraud
Not Fraud
...
```

for every transaction.

Accuracy:

```python
95%
```

Looks excellent but:

```python
Fraud Detection = 0%
```

The model completely fails.

---

# Common Real-World Examples

### Fraud Detection

```python
Fraud Transactions = Very Few
Normal Transactions = Very Many
```

### Disease Prediction

```python
Disease Cases = Rare
Healthy Cases = Common
```

### Spam Detection

```python
Spam Emails = Few
Normal Emails = Many
```

### Defect Detection

```python
Defective Products = Few
Good Products = Many
```

---

# Types of Class Imbalance

## 1. Mild Imbalance

```python
60 : 40
70 : 30
```

Usually manageable.

---

## 2. Moderate Imbalance

```python
80 : 20
90 : 10
```

May require balancing techniques.

---

## 3. Severe Imbalance

```python
99 : 1
999 : 1
```

Needs special handling.

---

# How to Detect Class Imbalance

Using Pandas:

```python
df["target"].value_counts()
```

Example:

```python
0    950
1     50
```

Percentage:

```python
df["target"].value_counts(normalize=True)*100
```

Output:

```python
0    95%
1     5%
```

---

# Evaluation Metrics for Imbalanced Data

Do NOT rely only on:

```python
Accuracy
```

Use:

* Precision
* Recall
* F1 Score
* ROC-AUC
* PR-AUC

---

# Precision

Measures:

```python
Out of predicted positives,
how many were actually positive?
```

Formula:

:contentReference[oaicite:0]{index=0}

High Precision:

```python
Few False Positives
```

---

# Recall

Measures:

```python
Out of actual positives,
how many were found?
```

Formula:

:contentReference[oaicite:1]{index=1}

High Recall:

```python
Few False Negatives
```

---

# F1 Score

Balances Precision and Recall.

Formula:

:contentReference[oaicite:2]{index=2}

Best metric when classes are imbalanced.

---

# Techniques to Handle Class Imbalance

## 1. Random Oversampling

Increase minority class samples.

Example:

Before:

```python
Class 0 = 950
Class 1 = 50
```

After:

```python
Class 0 = 950
Class 1 = 950
```

### Advantages

* Simple
* Keeps all data

### Disadvantages

* Can cause overfitting

---

## 2. Random Undersampling

Reduce majority class samples.

Before:

```python
950 : 50
```

After:

```python
50 : 50
```

### Advantages

* Faster training

### Disadvantages

* Information loss

---

## 3. SMOTE

Full Form:

```python
Synthetic Minority Oversampling Technique
```

Creates synthetic minority samples.

Example:

```python
Original Minority Samples
↓
Generate Similar New Samples
↓
Balanced Dataset
```

### Advantages

* Better than random duplication
* Widely used

### Disadvantages

* Can generate noisy samples

---

## 4. ADASYN

Full Form:

```python
Adaptive Synthetic Sampling
```

Improved version of SMOTE.

Focuses more on difficult minority samples.

### Best Use

```python
Highly Imbalanced Datasets
```

---

## 5. Class Weights

Give more importance to minority class.

Example:

```python
Class 0 Weight = 1
Class 1 Weight = 20
```

Model penalizes mistakes on minority class more heavily.

### Python

```python
model.fit(
    X_train,
    y_train,
    class_weight="balanced"
)
```

### Advantages

* No data duplication
* Very effective

---

## 6. Ensemble Methods

Use multiple models.

Examples:

```python
Balanced Random Forest
EasyEnsemble
XGBoost
LightGBM
```

Often perform well on imbalanced datasets.

---

# Popular Techniques by Algorithm

| Algorithm | Recommended Method |
|------------|-------------------|
| Logistic Regression | Class Weights |
| SVM | Class Weights |
| Random Forest | Balanced RF / SMOTE |
| XGBoost | scale_pos_weight |
| LightGBM | is_unbalance |
| Deep Learning | Class Weights + Focal Loss |

---

# Deep Learning Solutions

## Class Weights

Give higher penalty to minority class errors.

---

## Focal Loss

Focuses learning on hard examples.

Used heavily in:

```python
Object Detection
Medical Imaging
Fraud Detection
```

---

# Simple Analogy

Suppose:

```python
1000 students
```

Only:

```python
20 failed
980 passed
```

If teacher predicts:

```python
Everyone Passed
```

Accuracy:

```python
98%
```

But failed students are never identified.

This is exactly the class imbalance problem.

---

# Final Summary

| Concept | Meaning |
|----------|----------|
| Class Imbalance | Unequal class distribution |
| Main Problem | Model favors majority class |
| Accuracy | Often misleading |
| Better Metrics | Precision, Recall, F1 |
| Oversampling | Add minority samples |
| Undersampling | Remove majority samples |
| SMOTE | Generate synthetic samples |
| Class Weights | Penalize minority mistakes more |
| Best Practice | Use F1 + SMOTE/Class Weights |
