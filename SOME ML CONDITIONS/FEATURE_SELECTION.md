# Feature Selection

Feature Selection is the process of selecting the most important features and removing unnecessary features from a dataset.

Because of this:

* Model trains faster
* Overfitting decreases
* Accuracy may improve
* Model becomes easier to understand

---

# Simple Example

Suppose you want to predict:

```python
House Price
```

Dataset:

```python
Area
Bedrooms
Bathrooms
Owner Name
House ID
```

Useful Features:

```python
Area
Bedrooms
Bathrooms
```

Unnecessary Features:

```python
Owner Name
House ID
```

Removing unnecessary features is Feature Selection.

---

# Why Feature Selection Is Important

Problems with too many features:

* Slower training
* More memory usage
* Increased overfitting
* Difficult interpretation

---

# Types of Feature Selection

### 1. Filter Methods

### 2. Wrapper Methods

### 3. Embedded Methods

---

# 1. Filter Methods

Features are selected before model training.

Uses statistical techniques.

### Examples

* Correlation
* Chi-Square Test
* ANOVA
* Mutual Information

---

## Correlation Method

Used mainly for:

```python
Numerical Features
```

Example:

| Feature | Correlation with Price |
|----------|----------------------|
| Area | 0.90 |
| Bedrooms | 0.75 |
| House ID | 0.02 |

Keep:

```python
Area
Bedrooms
```

Remove:

```python
House ID
```

---

## Chi-Square Test

Used for:

```python
Categorical Features
```

Example:

```python
Gender
City
Education
```

Measures relationship with target variable.

Higher Chi-Square score:

```python
More Important Feature
```

---

## Mutual Information

Measures how much information a feature provides about the target.

Example:

```python
Area → High Information
House ID → Low Information
```

Keep features with higher scores.

---

# 2. Wrapper Methods

Model itself evaluates feature combinations.

More accurate but slower.

---

## Forward Selection

Starts with:

```python
No Features
```

Adds one feature at a time.

Example:

```python
Area
↓
Area + Bedrooms
↓
Area + Bedrooms + Bathrooms
```

Stops when no improvement occurs.

---

## Backward Elimination

Starts with:

```python
All Features
```

Removes least useful features one by one.

Example:

```python
Area
Bedrooms
Bathrooms
House ID
Owner Name
```

Remove:

```python
House ID
```

Then:

```python
Owner Name
```

---

## Recursive Feature Elimination (RFE)

Most popular wrapper method.

Steps:

```python
Train Model
↓
Find Least Important Feature
↓
Remove It
↓
Repeat
```

---

# 3. Embedded Methods

Feature selection happens during model training.

Fast and powerful.

---

## Lasso Regression

Lasso automatically reduces some coefficients to zero.

Example:

```python
Area      = 0.85
Bedrooms  = 0.42
House ID  = 0.00
```

Feature with:

```python
0.00
```

can be removed.

---

## Tree-Based Models

Examples:

```python
Decision Tree
Random Forest
XGBoost
```

Provide Feature Importance.

Example:

| Feature | Importance |
|----------|------------|
| Area | 0.65 |
| Bedrooms | 0.25 |
| House ID | 0.01 |

Remove:

```python
House ID
```

---

# Feature Selection vs Feature Extraction

| Feature Selection | Feature Extraction |
|------------------|-------------------|
| Keeps Original Features | Creates New Features |
| Removes Unnecessary Columns | Transforms Features |
| Easy to Interpret | Harder to Interpret |

---

# Example

Original Features:

```python
Area
Bedrooms
Bathrooms
House ID
```

Feature Selection:

```python
Area
Bedrooms
Bathrooms
```

Feature Extraction:

```python
PCA Component 1
PCA Component 2
```

---

# Real-Life Example

Student Performance Prediction:

Dataset:

```python
Study Hours
Attendance
Marks
Student ID
Mobile Number
```

Useful:

```python
Study Hours
Attendance
```

Remove:

```python
Student ID
Mobile Number
```

---

# Popular Methods for Interviews

| Method | Category |
|----------|-----------|
| Correlation | Filter |
| Chi-Square | Filter |
| Mutual Information | Filter |
| Forward Selection | Wrapper |
| Backward Elimination | Wrapper |
| RFE | Wrapper |
| Lasso | Embedded |
| Random Forest Importance | Embedded |

---

# Simple Analogy

Suppose you are packing a travel bag.

Useful Items:

```python
Clothes
Wallet
Phone
```

Unnecessary Items:

```python
Old Bills
Broken Charger
```

Removing unnecessary items is like Feature Selection.

---

# Final Summary

| Concept | Meaning |
|----------|----------|
| Feature Selection | Selecting important features |
| Goal | Improve model performance |
| Benefits | Faster training, less overfitting |
| Filter Methods | Correlation, Chi-Square, MI |
| Wrapper Methods | Forward, Backward, RFE |
| Embedded Methods | Lasso, Random Forest |
| Most Popular | Correlation, RFE, Lasso |

---

# One-Line Definition

```python
Feature Selection is the process of choosing the most relevant features and removing unnecessary ones to improve model performance and reduce complexity.
```