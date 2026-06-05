# Random Forest Regressor

## Model Type

- Supervised Machine Learning Model
- Regression Algorithm
- Ensemble Learning Algorithm
- Tree-Based Model

---

## Most Common Use Cases

- House Price Prediction
- Sales Forecasting
- Demand Forecasting
- Revenue Prediction
- Stock Trend Analysis
- Customer Lifetime Value Prediction

Used when the target/output is a continuous numerical value and the data contains complex non-linear relationships.

---

## Definition

Random Forest Regressor is an ensemble learning algorithm that combines multiple Decision Trees and averages their predictions to produce the final output.

Instead of relying on a single tree, it uses the collective prediction of many trees, making it more accurate and robust.

---

## Import

```python
from sklearn.ensemble import RandomForestRegressor
```

---

## Training

```python
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
```

---

## Prediction

```python
predictions = model.predict(X_test)
```

---

## How It Works

Suppose 5 trees predict:

```text
Tree 1 → 20,00,000
Tree 2 → 22,00,000
Tree 3 → 21,00,000
Tree 4 → 23,00,000
Tree 5 → 24,00,000
```

Final Prediction:

```text
(20 + 22 + 21 + 23 + 24) / 5

= 22,00,000
```

The model averages predictions from all trees.

---

## Why Do We Need It?

A single Decision Tree often overfits.

Random Forest solves this by:

- Creating multiple trees
- Training each tree on different subsets of data
- Combining predictions

This reduces variance and improves generalization.

---

## Advantages

- High accuracy
- Handles non-linear relationships
- Less prone to overfitting than Decision Trees
- Works well with large datasets
- Handles feature interactions automatically
- No feature scaling required

---

## Limitations

- Slower than a single Decision Tree
- Uses more memory
- Less interpretable
- Training time increases with more trees

---

## Underfitting or Overfitting?

### Overfitting: Possible but Less Common

Occurs when:

```python
max_depth=None
n_estimators very high
```

Reason:

Individual trees may memorize patterns.

However, averaging significantly reduces overfitting compared to a single Decision Tree.

Result:

- Low training error
- Slightly higher testing error

---

### Underfitting: Possible

Occurs when:

```python
max_depth=2
n_estimators=5
```

Reason:

Trees become too simple and cannot learn complex relationships.

Result:

- High training error
- High testing error

---

## Important Hyperparameters

### Number of Trees

```python
n_estimators=100
```

- More Trees → Better Stability
- More Trees → Higher Computation Cost

---

### Maximum Depth

```python
max_depth=10
```

Controls how deep each tree can grow.

- Small Depth → Underfitting
- Large Depth → Overfitting

---

### Minimum Samples Split

```python
min_samples_split=2
```

Minimum samples required to split a node.

---

### Minimum Samples Leaf

```python
min_samples_leaf=1
```

Minimum samples required in a leaf node.

---

## Why Feature Scaling Is Not Required?

Random Forest uses decision trees.

Trees split data based on conditions like:

```text
Age > 30
Income > 50000
```

No distance calculations are performed.

Therefore:

- StandardScaler not required
- MinMaxScaler not required

---

## When Should You Use It?

Use when:

- Output is continuous
- Data contains non-linear relationships
- High accuracy is needed
- Interpretability is not the main priority

---

## When Should You Avoid It?

Avoid when:

- Fast training is critical
- Model explainability is required
- Dataset is extremely large

Consider:

- Linear Regression
- Decision Tree Regressor
- XGBoost Regressor

---

## Why Is It Better Than Decision Tree?

- Less overfitting
- Better generalization
- More stable predictions
- Higher accuracy

---

## Why Is It Better Than Linear Regression?

- Captures complex non-linear patterns
- No assumption of linear relationships
- Handles feature interactions automatically

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

"Random Forest Regressor is an ensemble learning algorithm that combines multiple Decision Trees and averages their predictions to accurately predict continuous values while reducing overfitting."