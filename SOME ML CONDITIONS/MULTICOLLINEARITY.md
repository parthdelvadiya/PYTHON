# Multicollinearity

Multicollinearity occurs when two or more independent features are highly correlated with each other.

Because of this:

* Model gets confused about feature importance
* Coefficients become unstable
* Interpretation becomes difficult

---

# Simple Example

Suppose a house price dataset contains:

```python
House Area (sq ft)
Number of Rooms
```

Larger houses usually have more rooms.

```python
Area ↑ → Rooms ↑
```

Both features carry almost the same information.

This is multicollinearity.

---

# Example Dataset

| Area | Rooms | Price |
|--------|--------|--------|
| 1000 | 2 | 20L |
| 1500 | 3 | 30L |
| 2000 | 4 | 40L |
| 2500 | 5 | 50L |

Here:

```python
Area and Rooms are highly correlated
```

---

# Why It Is a Problem

Model cannot easily determine:

```python
Price increased because of Area
OR
Price increased because of Rooms
```

Both variables explain the same thing.

---

# Models Affected Most

### Highly Affected

```python
Linear Regression
Logistic Regression
```

### Less Affected

```python
Decision Tree
Random Forest
XGBoost
```

Tree-based models handle it much better.

---

# How to Detect Multicollinearity

## 1. Correlation Matrix

```python
df.corr()
```

Example:

| Feature | Area | Rooms |
|----------|------|--------|
| Area | 1.00 | 0.95 |
| Rooms | 0.95 | 1.00 |

Rule:

```python
Correlation > 0.8
```

Possible multicollinearity.

---

## 2. VIF (Variance Inflation Factor)

Most common method.

Formula:

```python
VIF = 1 / (1 - R²)
```

### Interpretation

| VIF | Meaning |
|------|----------|
| 1 | No Correlation |
| 1-5 | Moderate Correlation |
| > 5 | High Correlation |
| > 10 | Serious Problem |

---

# How to Remove Multicollinearity

## Method 1

Remove one of the correlated features.

Example:

```python
Area
Rooms
```

Keep:

```python
Area
```

Remove:

```python
Rooms
```

---

## Method 2

Feature Engineering

Example:

Instead of:

```python
Length
Width
```

Create:

```python
Area = Length × Width
```

---

## Method 3

Use Regularization

```python
Ridge Regression
Lasso Regression
```

These reduce the impact of multicollinearity.

---

# Real-Life Example

Suppose employee salary prediction contains:

```python
Years of Experience
Age
```

Usually:

```python
Age ↑ → Experience ↑
```

Both are highly related.

This can create multicollinearity.

---

# Simple Analogy

Suppose you ask:

```python
How tall is a person?
```

And collect:

```python
Height in cm
Height in meters
```

Both provide the same information.

Using both is unnecessary.

This is similar to multicollinearity.

---

# Final Summary

| Concept | Meaning |
|----------|----------|
| Multicollinearity | Features highly correlated with each other |
| Main Problem | Difficult feature interpretation |
| Affects Most | Linear & Logistic Regression |
| Detection | Correlation Matrix, VIF |
| Correlation Warning | > 0.8 |
| Serious VIF | > 10 |
| Solution | Remove features, Feature Engineering, Ridge/Lasso |

---

# One-Line Definition

```python
Multicollinearity occurs when independent features are highly correlated with each other, causing unstable model coefficients and difficult interpretation.
```