# Decision Tree Regressor

## Model Type

- Supervised Machine Learning Model
- Regression Algorithm
- Non-Parametric Model
- Tree-Based Algorithm

---

## Most Common Use Cases

- House Price Prediction
- Sales Forecasting
- Demand Forecasting
- Revenue Prediction
- Energy Consumption Prediction
- Any regression problem with non-linear relationships

Used when the target/output is a continuous numerical value.

---

## Definition

Decision Tree Regressor predicts a continuous value by recursively splitting the dataset into smaller regions and assigning the average target value of each region as the prediction.

Unlike Linear Regression, it does not fit a straight line and can learn complex non-linear patterns.

---

## Import

```python
from sklearn.tree import DecisionTreeRegressor
```

---

## Training

```python
model = DecisionTreeRegressor(random_state=42)

model.fit(X_train, y_train)
```

---

## Prediction

```python
predictions = model.predict(X_test)
```

---

## How It Works

The model creates decision rules based on feature values.

Example:

```text
Area > 1500 sq ft?
│
├── Yes
│   └── Predicted Price = ₹75,00,000
│
└── No
    └── Predicted Price = ₹40,00,000
```

The tree keeps splitting until a stopping condition is reached.

Final prediction is usually the average target value of samples in the leaf node.

---

## Why Do We Need It?

Many real-world datasets have complex non-linear relationships.

Decision Trees can:

- Learn non-linear patterns
- Handle feature interactions
- Work without feature scaling
- Be easily visualized and interpreted

---

## Advantages

- Handles non-linear data well
- Easy to understand and visualize
- No feature scaling required
- Works with numerical and categorical data
- Captures feature interactions automatically

---

## Limitations

- Very prone to overfitting
- Unstable (small data changes can create different trees)
- Can memorize training data
- Lower generalization compared to ensemble methods

---

## Underfitting or Overfitting?

### Overfitting: Very Common

Occurs when:

```python
max_depth=None
```

Reason:

The tree keeps growing until it memorizes the training data.

Result:

- Very low training error
- High testing error

---

### Underfitting: Possible

Occurs when:

```python
max_depth=2
```

Reason:

The tree is too small to capture important patterns.

Result:

- High training error
- High testing error

---

## Important Hyperparameters

### Max Depth

```python
DecisionTreeRegressor(max_depth=5)
```

Controls maximum tree depth.

- Small Depth → Underfitting
- Large Depth → Overfitting

---

### Min Samples Split

```python
min_samples_split=2
```

Minimum samples required to split a node.

---

### Min Samples Leaf

```python
min_samples_leaf=1
```

Minimum samples required in a leaf node.

---

## Why Feature Scaling Is Not Required?

Decision Trees split based on conditions:

```text
Age > 30
Salary > 50000
```

They do not use distance calculations.

Therefore:

- StandardScaler not required
- MinMaxScaler not required

---

## When Should You Use It?

Use when:

- Output is continuous
- Data has non-linear patterns
- Interpretability is important
- Feature scaling is not desired

---

## When Should You Avoid It?

Avoid when:

- Dataset is very noisy
- High generalization is required
- Overfitting becomes a major issue

Consider:

- Random Forest Regressor
- XGBoost Regressor
- Gradient Boosting Regressor

---

## Why Is It Better Than Linear Regression?

- Learns non-linear relationships
- No assumption of linearity
- Handles complex interactions automatically

---

## Why Is It Better Than KNN Regression?

- Faster predictions
- No distance calculations
- No feature scaling required

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

"Decision Tree Regressor is a supervised tree-based regression algorithm that predicts continuous values by recursively splitting data into regions and using the average target value of each leaf node as the prediction."