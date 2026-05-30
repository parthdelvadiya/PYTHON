# Data Drift vs Model Drift

Drift occurs when real-world data changes over time, causing model performance to degrade.

---

# 1. Data Drift

Data Drift happens when the input data distribution changes compared to the training data.

### Example

Model trained on:

```python
Age: 20-40
```

New production data:

```python
Age: 50-80
```

Input data has changed.

This is:

```python
Data Drift
```

---

# Real-Life Example

Fraud Detection Model:

Training Data:

```python
Fraud patterns from 2024
```

Production Data:

```python
New fraud techniques in 2026
```

Input behavior changes.

---

# Problem

```python
Model sees unfamiliar data
↓
Accuracy decreases
```

---

# 2. Model Drift

Model Drift happens when the relationship between inputs and outputs changes over time.

### Example

House Price Model:

Training:

```python
Area → Price
```

After several years:

```python
Location becomes more important than Area
```

The learned relationship is no longer valid.

This is:

```python
Model Drift
```

---

# Real-Life Example

Spam Detection:

Old Rule:

```python
Certain keywords = Spam
```

Spammers start using new words.

The model's learned patterns become outdated.

---

# Data Drift vs Model Drift

| Feature | Data Drift | Model Drift |
|----------|------------|-------------|
| What Changes? | Input Data | Input-Output Relationship |
| Example | Different Customer Ages | Customer Behavior Changes |
| Effect | Unfamiliar Inputs | Wrong Predictions |
| Solution | Retrain with New Data | Retrain/Rebuild Model |

---

# How to Detect Drift

### Data Drift

Compare:

```python
Training Data
vs
Production Data
```

Check:

* Mean
* Distribution
* Feature Statistics

---

### Model Drift

Monitor:

```python
Accuracy
Precision
Recall
F1 Score
```

If performance drops consistently:

```python
Possible Model Drift
```

---

# How to Handle Drift

### Data Drift

```python
Collect New Data
Retrain Model
Update Features
```

### Model Drift

```python
Retrain Model
Fine-Tune Model
Build New Model
```

---

# Simple Analogy

Suppose you learned:

```python
Exam Pattern 2024
```

But in 2026:

```python
Questions become completely different
```

Question style changed:

```python
Data Drift
```

Old preparation strategy no longer works:

```python
Model Drift
```

---

# Final Summary

| Concept | Meaning |
|----------|----------|
| Data Drift | Input data distribution changes |
| Model Drift | Relationship between input and output changes |
| Main Effect | Performance degradation |
| Detection | Monitor data & metrics |
| Solution | Retraining and updating models |

---

# One-Line Definitions

```python
Data Drift: Input data distribution changes over time.
```

```python
Model Drift: Model predictions become less accurate because learned patterns no longer match reality.
```