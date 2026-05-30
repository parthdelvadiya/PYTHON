# StandardScaler vs MinMaxScaler

Feature Scaling is used to bring numerical features to a similar scale.

Without scaling:

* Large values can dominate small values
* Distance-based algorithms may perform poorly
* Training can become slower

---

# StandardScaler

StandardScaler transforms data so that:

* Mean = 0
* Standard Deviation = 1

Formula:

\[
z = \frac{x - \mu}{\sigma}
\]

Where:

* x = Original value
* μ = Mean
* σ = Standard deviation

---

# Example

Original Data:

```python
[10, 20, 30, 40, 50]
```

After StandardScaler:

```python
[-1.41, -0.71, 0.00, 0.71, 1.41]
```

Properties:

* Mean becomes 0
* Values can be negative
* No fixed range

---

# When to Use StandardScaler

Best for:

* Logistic Regression
* Linear Regression
* KNN
* SVM
* Neural Networks

When data follows approximately normal distribution.

---

# MinMaxScaler

MinMaxScaler rescales values into a fixed range.

Usually:

```python
0 to 1
```

Formula:

\[
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
\]

---

# Example

Original Data:

```python
[10, 20, 30, 40, 50]
```

After MinMaxScaler:

```python
[0.00, 0.25, 0.50, 0.75, 1.00]
```

Properties:

* Values stay between 0 and 1
* Easy to interpret
* Sensitive to outliers

---

# When to Use MinMaxScaler

Best for:

* Deep Learning
* Neural Networks
* Image Processing
* Data with known boundaries

When preserving relative relationships is important.

---

# Outlier Example

Data:

```python
[10, 20, 30, 40, 1000]
```

MinMaxScaler:

```python
[0.00, 0.01, 0.02, 0.03, 1.00]
```

Most values get compressed near 0.

StandardScaler handles this situation better.

---

# StandardScaler vs MinMaxScaler

| Feature | StandardScaler | MinMaxScaler |
|----------|---------------|--------------|
| Mean | 0 | Not Fixed |
| Std Dev | 1 | Not Fixed |
| Range | No Fixed Range | 0 to 1 |
| Negative Values | Yes | No |
| Outlier Handling | Better | Sensitive |
| Common Use | ML Models | Deep Learning |

---

# Simple Analogy

Marks:

```python
[40, 50, 60, 70, 80]
```

StandardScaler:

```python
Shows how far each mark is from average
```

MinMaxScaler:

```python
Converts marks into a percentage-like scale
```

---

# Final Summary

| Scaler | Best Use |
|----------|----------|
| StandardScaler | Regression, KNN, SVM, ML Models |
| MinMaxScaler | Neural Networks, Image Data |
| StandardScaler | Better with Outliers |
| MinMaxScaler | Fixed Range (0-1) |