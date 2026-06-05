# XGBoost Regressor

## Model Type

- Supervised Machine Learning Model
- Regression Algorithm
- Ensemble Learning Algorithm
- Boosting Algorithm

---

## Most Common Use Cases

- House Price Prediction
- Sales Forecasting
- Demand Forecasting
- Revenue Prediction
- Customer Lifetime Value Prediction
- Kaggle Competitions
- Structured/Tabular Data Problems

Used when the target/output is a continuous numerical value and high prediction accuracy is required.

---

## Definition

XGBoost (Extreme Gradient Boosting) is an advanced boosting algorithm that builds Decision Trees sequentially.

Each new tree focuses on correcting the errors made by the previous trees.

The final prediction is the combined output of all trees.

---

## Import

```python
from xgboost import XGBRegressor
```

---

## Training

```python
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
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

### Step 1

First tree makes predictions.

```text
Actual Price = 20,00,000
Predicted = 18,00,000

Error = 2,00,000
```

---

### Step 2

Second tree learns this error.

```text
Correction = +1,50,000
```

---

### Step 3

Third tree learns the remaining error.

```text
Correction = +40,000
```

---

### Final Prediction

```text
Prediction =
Tree1 + Tree2 + Tree3 + ...
```

Each tree tries to reduce the mistakes of previous trees.

---

## Why Do We Need It?

Decision Trees often overfit.

Random Forest reduces overfitting by averaging many trees.

XGBoost improves performance further by:

- Learning from previous mistakes
- Optimizing errors using gradient descent
- Applying regularization

This usually results in higher accuracy.

---

## Advantages

- Very high accuracy
- Handles non-linear relationships
- Built-in regularization
- Handles missing values well
- Feature importance available
- Often wins machine learning competitions

---

## Limitations

- More complex to tune
- Slower training than Random Forest
- Requires hyperparameter tuning
- Less interpretable

---

## Underfitting or Overfitting?

### Overfitting: Possible

Occurs when:

```python
max_depth=20
n_estimators=1000
learning_rate=0.5
```

Reason:

The model becomes too complex and starts memorizing noise.

Result:

- Very low training error
- High testing error

---

### Underfitting: Possible

Occurs when:

```python
max_depth=2
n_estimators=10
```

Reason:

The model is too simple to learn patterns.

Result:

- High training error
- High testing error

---

## Important Hyperparameters

### Number of Trees

```python
n_estimators=100
```

- More Trees → Better Learning
- Too Many Trees → Overfitting Risk

---

### Learning Rate

```python
learning_rate=0.1
```

Controls how much each tree contributes.

- Small Value → Slower Learning
- Large Value → Faster Learning but higher overfitting risk

---

### Maximum Depth

```python
max_depth=6
```

Controls tree complexity.

- Small Depth → Underfitting
- Large Depth → Overfitting

---

### Subsample

```python
subsample=0.8
```

Uses only a portion of training data for each tree.

Helps reduce overfitting.

---

## Why Feature Scaling Is Not Required?

XGBoost is based on Decision Trees.

Trees use split conditions:

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
- High accuracy is required
- Dataset is structured/tabular
- Computational resources are available

---

## When Should You Avoid It?

Avoid when:

- Model interpretability is the main goal
- Dataset is extremely small
- Fast experimentation is more important than accuracy

Consider:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## Why Is It Better Than Decision Tree?

- Much less overfitting
- Better generalization
- Higher accuracy

---

## Why Is It Better Than Random Forest?

- Learns from previous errors
- Usually achieves higher accuracy
- Requires fewer trees for similar performance

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

"XGBoost Regressor is a boosting-based ensemble algorithm that builds Decision Trees sequentially, where each new tree learns from the errors of previous trees to improve prediction accuracy for continuous values."