# Encoding Techniques in Machine Learning & Deep Learning

Encoding converts categorical (text) data into numerical form so ML and DL models can understand it.

---

# Why Encoding is Needed

Machine Learning models cannot directly process:

```python
Red
Blue
Green
```

Models require:

```python
0
1
2
```

or

```python
[1,0,0]
[0,1,0]
[0,0,1]
```

---

# 1. Label Encoding

Each category receives a unique number.

### Example

```python
Red   -> 0
Blue  -> 1
Green -> 2
```

### Advantages

* Simple
* Fast
* Memory efficient

### Disadvantages

Creates artificial ordering.

```python
Green > Blue > Red
```

which may not be true.

### Best Use

```python
Target Variables
Yes/No
Pass/Fail
Spam/Not Spam
```

---

# 2. Ordinal Encoding

Used when categories have a natural order.

### Example

```python
Low     -> 1
Medium  -> 2
High    -> 3
```

### Advantages

* Preserves order
* Easy to understand

### Disadvantages

Distances between values may not be meaningful.

### Best Use

```python
Education Levels
Ratings
Sizes
```

---

# 3. One-Hot Encoding

Creates separate columns for each category.

### Example

```python
City = Ahmedabad
```

| Ahmedabad | Surat | Rajkot |
|------------|--------|---------|
| 1 | 0 | 0 |

### Advantages

* No false ordering
* Most popular encoding

### Disadvantages

Many categories create many columns.

### Best Use

```python
City
Country
Color
Gender
```

---

# 4. Dummy Encoding

One-Hot Encoding with one column removed.

### Example

Instead of:

| Male | Female |
|--------|--------|
| 1 | 0 |
| 0 | 1 |

Use:

| Male |
|--------|
| 1 |
| 0 |

### Advantages

* Reduces redundancy
* Avoids Dummy Variable Trap

### Best Use

```python
Linear Regression
Logistic Regression
```

---

# 5. Binary Encoding

Categories are converted into binary numbers.

### Example

```python
A -> 1 -> 001
B -> 2 -> 010
C -> 3 -> 011
D -> 4 -> 100
```

### Advantages

* Fewer columns than One-Hot
* Handles large categories well

### Best Use

```python
Product IDs
User IDs
Large Category Features
```

---

# 6. Frequency Encoding

Replace category with occurrence frequency.

### Example

```python
Ahmedabad -> 60%
Surat     -> 25%
Rajkot    -> 15%
```

Encoded:

```python
60
25
15
```

### Advantages

* Simple
* Handles many categories

### Best Use

```python
Large Datasets
Tree-Based Models
```

---

# 7. Count Encoding

Replace category by count.

### Example

```python
Ahmedabad -> 300
Surat     -> 120
Rajkot    -> 50
```

### Advantages

* Easy implementation
* Useful for high-cardinality features

### Best Use

```python
Random Forest
XGBoost
LightGBM
```

---

# 8. Target Encoding

Replace category using target mean.

### Example

Loan Approval:

```python
Ahmedabad -> 0.75
Surat     -> 0.40
Rajkot    -> 0.20
```

### Advantages

* Powerful
* Improves model performance

### Disadvantages

* Risk of Data Leakage

### Best Use

```python
High Cardinality Features
Kaggle Competitions
```

---

# 9. Mean Encoding

Similar to Target Encoding.

Uses average target value.

### Example

House Prices:

```python
Area A -> 500000
Area B -> 700000
Area C -> 300000
```

### Best Use

```python
Regression Problems
```

---

# 10. Hash Encoding

Uses hash functions to create fixed columns.

### Example

```python
Ahmedabad -> Column 2
Surat     -> Column 5
Rajkot    -> Column 1
```

### Advantages

* Fixed memory usage
* Very scalable

### Disadvantages

* Hash collisions possible

### Best Use

```python
Big Data
Streaming Data
```

---

# 11. Leave-One-Out Encoding

Improved version of Target Encoding.

Current row is excluded when calculating target mean.

### Advantage

Reduces overfitting.

### Best Use

```python
Competition Datasets
High Cardinality Features
```

---

# 12. Weight of Evidence (WOE) Encoding

Widely used in finance and risk modeling.

Formula:

```python
WOE = ln(Good% / Bad%)
```

### Example

```python
Category A = 0.85
Category B = -0.40
```

### Advantages

* Handles categorical variables well
* Easy interpretation

### Best Use

```python
Credit Scoring
Risk Analysis
Fraud Detection
```

---

# 13. Embedding Encoding (Deep Learning)

Deep Learning learns dense vector representations automatically.

### Example

Word:

```python
King
```

Embedding:

```python
[0.25, -0.81, 0.47, 1.12]
```

### Advantages

* Captures relationships
* Handles huge vocabularies
* Low dimensional

### Best Use

```python
NLP
Recommendation Systems
Deep Learning Models
```

---

# Which Encoding Should You Use?

| Situation | Recommended Encoding |
|------------|---------------------|
| Binary Categories | Label Encoding |
| Ordered Categories | Ordinal Encoding |
| Small Categories | One-Hot Encoding |
| Regression Models | Dummy Encoding |
| Many Categories | Binary Encoding |
| Very Large Categories | Frequency Encoding |
| Tree Models | Count Encoding |
| High Cardinality Features | Target Encoding |
| Big Data | Hash Encoding |
| Financial Models | WOE Encoding |
| Deep Learning & NLP | Embeddings |

---

# Quick Summary

| Encoding | Main Idea |
|-----------|------------|
| Label | Category → Number |
| Ordinal | Ordered Category → Number |
| One-Hot | Category → Separate Columns |
| Dummy | One-Hot Minus One Column |
| Binary | Category → Binary Values |
| Frequency | Category → Frequency % |
| Count | Category → Count |
| Target | Category → Target Mean |
| Mean | Category → Average Target |
| Hash | Category → Hash Bucket |
| Leave-One-Out | Safer Target Encoding |
| WOE | Risk-Based Encoding |
| Embedding | Learned Dense Vectors |

---

# Final Summary

Encoding transforms categorical data into numerical form for ML and DL models.

Most commonly used:

```python
One-Hot Encoding
Label Encoding
Ordinal Encoding
```

For large datasets:

```python
Target Encoding
Frequency Encoding
Hash Encoding
```

For Deep Learning:

```python
Embedding Layers
```