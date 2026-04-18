# Artificial Neural Network (ANN) – Complete Implementation and Interview Guide

---

## 1. What is ANN?

Artificial Neural Network (ANN) is a **Deep Learning model** inspired by the human brain.

It consists of multiple layers of neurons that learn patterns from data.

ANN is mainly used for:

- Classification
- Regression
- Pattern recognition
- Complex nonlinear relationships

---

## 2. Real-world Examples

- Spam email detection
- Customer churn prediction
- Disease prediction
- House price prediction
- Image classification

---

## 3. Basic Structure of ANN

ANN mainly has 3 types of layers:

### 3.1 Input Layer
Receives input features.

Example:
- age
- salary
- experience

---

### 3.2 Hidden Layer
Learns complex patterns and relationships.

This is where actual learning happens.

---

### 3.3 Output Layer
Gives final prediction.

Example:
- 0 → No
- 1 → Yes

---

## 4. Important Terms

| Term | Meaning |
|-------|----------|
| Neuron | Basic processing unit |
| Weight | Importance of input |
| Bias | Additional constant value |
| Activation Function | Decides output |
| Epoch | One full training cycle |
| Loss Function | Measures error |

---

## 5. Mathematical Equation

Each neuron works like:

y = w1x1 + w2x2 + ... + b

Then activation function is applied.

For example:

A = activation(wx + b)

Where:

- x → input
- w → weights
- b → bias
- A → output

---

## 6. Activation Functions

### ReLU
Used in hidden layers.

f(x) = max(0, x)

:contentReference[oaicite:0]{index=0}

---

### Sigmoid
Used in binary classification output layer.

f(x) = 1 / (1 + e^-x)


::contentReference[oaicite:1]{index=1}


Output range: 0 to 1

---

## 7. Complete Implementation (ANN Classification)

```python
# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ==============================
# 2. Load Dataset
# ==============================
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Dataset Shape:", X.shape)


# ==============================
# 3. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==============================
# 4. Feature Scaling
# ==============================
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ==============================
# 5. Build ANN Model
# ==============================
model = Sequential()

# Input + Hidden Layer 1
model.add(Dense(16, activation='relu', input_shape=(X_train.shape[1],)))

# Hidden Layer 2
model.add(Dense(8, activation='relu'))

# Output Layer
model.add(Dense(1, activation='sigmoid'))


# ==============================
# 6. Compile Model
# ==============================
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)


# ==============================
# 7. Train Model
# ==============================
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2
)


# ==============================
# 8. Predictions
# ==============================
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)


# ==============================
# 9. Evaluation
# ==============================
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

---

## 8. Why Feature Scaling is Important?

ANN is very sensitive to feature values.

If one feature is:

salary = 50000

and another is:

age = 25

then training becomes unstable.

So we use:

```python
StandardScaler()
```

This makes all features on similar scale.

---

## 9. Important Parameters

### Dense(16)
16 neurons in layer.

---

### activation='relu'
Used for learning nonlinear patterns.

---

### optimizer='adam'
Used for updating weights.

Very commonly asked in interviews.

---

### loss='binary_crossentropy'
Used for binary classification.

---

### epochs=20
Model sees entire dataset 20 times.

---

### batch_size=32
Processes 32 rows at once.

---

## 10. Overfitting vs Underfitting

### Overfitting
- Training accuracy high
- Testing accuracy low

Model memorizes data.

---

### Underfitting
- Both accuracies low

Model too simple.

---

## 11. Important Interview Questions

### 1. What is ANN?
ANN is a deep learning model made up of interconnected neurons used to learn complex patterns.

---

### 2. Why do we use activation functions?
Without activation functions, ANN behaves like linear regression.

Activation introduces nonlinearity.

---

### 3. Why ReLU?
ReLU is fast and solves vanishing gradient problem better than sigmoid.

---

### 4. Why sigmoid in output?
For binary classification, output must be between 0 and 1.

---

### 5. Why feature scaling?
To ensure stable and faster learning.

---

### 6. What is epoch?
One complete pass over training data.

---

### 7. What is batch size?
Number of samples processed at one time.

---

## Final Interview Summary

ANN is a deep learning model used to learn complex nonlinear relationships.

It contains:

- input layer
- hidden layers
- output layer

Important concepts:

- weights
- bias
- activation function
- optimizer
- loss function
- epochs

ANN is widely used in classification and regression tasks.