# K-Nearest Neighbors (KNN) Regression

## Model Type

- Supervised Machine Learning Model
- Regression Algorithm
- Non-Parametric Model
- Instance-Based (Lazy Learning) Algorithm

---

## Most Common Use Cases

- House Price Prediction
- Sales Forecasting
- Temperature Prediction
- Stock Trend Prediction
- Demand Forecasting
- Any regression problem with non-linear relationships

Used when the target/output is a continuous numerical value.

---

## Definition

KNN Regression predicts a continuous value by finding the K nearest data points and taking their average.

Unlike Linear Regression, it does not learn an equation. It stores the training data and makes predictions based on nearby samples.

---

## Import

```python
from sklearn.neighbors import KNeighborsRegressor
```

---

## Training

```python
model = KNeighborsRegressor(n_neighbors=5)

model.fit(X_train, y_train)
```

---

## Prediction

```python
predictions = model.predict(X_test)
```

---

## How It Works

Suppose we want to predict a house price.

Nearest neighbors:

```text
₹20,00,000
₹22,00,000
₹21,00,000
```

Prediction:

```text
(20 + 22 + 21) / 3
= ₹21,00,000
```

The model predicts the average value of the nearest neighbors.

---

## Why Do We Need It?

Many real-world datasets have non-linear relationships.

Linear Regression tries to fit a line.

KNN Regression learns local patterns directly from nearby data points without assuming any specific relationship.

---

## Advantages

- Simple to understand
- No assumptions about data distribution
- Can model non-linear relationships
- No training complexity
- Works well on small datasets

---

## Limitations

- Slow prediction on large datasets
- Memory intensive
- Sensitive to irrelevant features
- Sensitive to feature scaling
- Performance decreases with high-dimensional data

---

## Underfitting or Overfitting?

### Overfitting: Common

Occurs when:

```python
n_neighbors = 1
```

Reason:

The model relies on a single nearest point and becomes highly sensitive to noise.

Result:

- Very low training error
- High testing error

---

### Underfitting: Common

Occurs when:

```python
n_neighbors = 50
```

Reason:

The model averages too many neighbors and ignores local patterns.

Result:

- High training error
- High testing error

---

## Important Hyperparameter

### K (Number of Neighbors)

```python
KNeighborsRegressor(n_neighbors=5)
```

- Small K → High Variance → Overfitting
- Large K → High Bias → Underfitting
- Moderate K → Better Generalization

---

## Why Feature Scaling Is Important?

KNN uses distance calculations.

Example:

```text
Age = 25
Salary = 500000
```

Salary values are much larger than age values.

Without scaling:

- Salary dominates distance calculations
- Model becomes biased

Therefore apply:

```python
from sklearn.preprocessing import StandardScaler
```

before training.

---

## When Should You Use It?

Use when:

- Output is continuous
- Dataset is small to medium-sized
- Relationship is non-linear
- Fast training is desired

---

## When Should You Avoid It?

Avoid when:

- Dataset is very large
- Number of features is very high
- Real-time prediction is required
- Memory is limited

Consider:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

---

## Why Is It Better Than Linear Regression?

- Captures non-linear relationships
- No assumption of linearity
- Can fit complex local patterns

---

## Why Is It Worse Than Linear Regression?

- Slower predictions
- Requires feature scaling
- Suffers from curse of dimensionality
- Memory intensive

---

## Evaluation Metrics

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```

Common Metrics:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Interview One-Liner

"KNN Regression is a supervised, non-parametric regression algorithm that predicts a continuous value by averaging the target values of the K nearest data points based on distance."