# Gradient Descent in Machine Learning

Gradient Descent is an optimization algorithm used to minimize the loss (error) of a machine learning model.

It helps the model find the best values of parameters (weights).

---

# Simple Intuition

Suppose you are standing on a mountain.

Your goal:

* reach the lowest point

What will you do?

* move step by step downward

Gradient Descent works exactly like this.

It moves step by step toward minimum error.

---

# Why Gradient Descent is Needed

Machine learning models try to minimize error.

Example:

```python id="9pxh2u"
Predicted Price != Actual Price
```

So the model adjusts weights repeatedly to reduce error.

Gradient Descent performs this adjustment automatically.

---

# Main Goal

Goal of Gradient Descent:

```python id="s1eq1l"
Find minimum loss/error
```

---

# Cost Function

Machine learning models use a cost function.

Example:

```math id="u98gl8"
J(θ) = (1/n) Σ(yᵢ - ŷᵢ)²
```

Where:

* J(θ) = cost function
* yᵢ = actual value
* ŷᵢ = predicted value

Gradient Descent minimizes this function.

---

# How Gradient Descent Works

Steps:

1. Initialize random weights
2. Calculate prediction
3. Compute error
4. Compute gradient
5. Update weights
6. Repeat until minimum error

---

# Weight Update Formula

Main formula:

```math id="6q7jlwm"
θ = θ - α(dJ/dθ)
```

Where:

* θ = weight/parameter
* α = learning rate
* dJ/dθ = gradient (slope)

---

# Understanding the Formula

Suppose:

```python id="s2dn0t"
Current weight = 10
Gradient = 2
Learning rate = 0.1
```

Update:

```python id="m4tvwa"
New weight = 10 - (0.1 × 2)
           = 9.8
```

Weights slowly move toward optimal values.

---

# What is Gradient?

Gradient means:

* slope
* direction of steepest increase

Gradient Descent moves in opposite direction.

Why?

Because we want minimum error.

---

# What is Learning Rate?

Learning rate controls step size.

Represented by:

```python id="c1sl0s"
alpha (α)
```

---

# Small Learning Rate

```python id="zjlwm2"
α = 0.0001
```

* very slow learning
* takes long time

---

# Large Learning Rate

```python id="f7o1rj"
α = 100
```

* jumps too much
* may never reach minimum

---

# Good Learning Rate

```python id="t85p7j"
α = 0.01
```

Usually balanced.

---

# Visual Understanding

Imagine:

```text id="72e3yi"
Large Step  -> may overshoot minimum
Small Step  -> very slow
Balanced Step -> reaches minimum efficiently
```

---

# Types of Gradient Descent

| Type                              | Description               |
| --------------------------------- | ------------------------- |
| Batch Gradient Descent            | Uses whole dataset        |
| Stochastic Gradient Descent (SGD) | Uses one sample at a time |
| Mini-Batch Gradient Descent       | Uses small batches        |

---

# 1. Batch Gradient Descent

Uses entire dataset for each update.

Example:

```python id="h2c7dt"
10000 rows → all used together
```

Advantages:

* stable updates

Disadvantages:

* slow for large datasets

---

# 2. Stochastic Gradient Descent (SGD)

Uses one sample at a time.

Example:

```python id="7dp0ol"
1 row → update weights
```

Advantages:

* fast
* works well for huge datasets

Disadvantages:

* noisy updates

---

# 3. Mini-Batch Gradient Descent

Uses small chunks of data.

Example:

```python id="q5xjlwm"
32 rows at once
```

Most commonly used in deep learning.

Advantages:

* faster
* stable
* memory efficient

---

# Example Using Linear Regression

Suppose equation:

```math id="o7s3ei"
y = wx + b
```

Initially:

```python id="x6mfjm"
w = 2
b = 1
```

Prediction error is high.

Gradient Descent updates:

* w
* b

again and again until error becomes small.

---

# Simple Python Example

```python id="bwzwdq"
import numpy as np

# Data
x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

# Initialize parameters
w = 0
b = 0

# Learning rate
lr = 0.01

# Training
for epoch in range(1000):

    y_pred = w * x + b

    # Gradients
    dw = (-2/len(x)) * np.sum(x * (y - y_pred))
    db = (-2/len(x)) * np.sum(y - y_pred)

    # Update parameters
    w = w - lr * dw
    b = b - lr * db

print("Weight:", w)
print("Bias:", b)
```

---

# Output

```python id="q7tjlwm"
Weight ≈ 2
Bias ≈ 0
```

Model successfully learns:

```python id="9lxm3p"
y = 2x
```

---

# Gradient Descent in Deep Learning

Gradient Descent is heavily used in:

* Neural Networks
* Deep Learning
* CNN
* RNN
* Transformers

Without Gradient Descent:

* neural networks cannot learn

---

# Gradient Descent + Backpropagation

In deep learning:

```text id="n5k7wq"
Forward Pass → Calculate Error
Backward Pass → Calculate Gradients
Gradient Descent → Update Weights
```

---

# Common Problems

# 1. Local Minimum

Model gets stuck in small minimum.

---

# 2. Vanishing Gradient

Gradients become extremely small.

Learning slows down.

Common in deep neural networks.

---

# 3. Exploding Gradient

Gradients become extremely large.

Weights become unstable.

---

# Optimizers Based on Gradient Descent

Advanced versions:

| Optimizer | Improvement            |
| --------- | ---------------------- |
| SGD       | Faster updates         |
| Momentum  | Reduces oscillation    |
| RMSProp   | Adaptive learning      |
| Adam      | Most popular optimizer |

---

# Adam Optimizer

Most used optimizer in deep learning.

Combines:

* Momentum
* RMSProp

Advantages:

* fast convergence
* stable learning
* adaptive learning rate

---

# TensorFlow Example

```python id="7hmdw0"
model.compile(
    optimizer='adam',
    loss='mse'
)
```

---

# PyTorch Example

```python id="6pzjlwm"
import torch.optim as optim

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)
```

---

# Real Life Analogy

Imagine blindfolded person climbing down mountain.

They:

* feel slope
* move downward step by step

This is Gradient Descent.

---

# Important Interview Questions

## Why Gradient Descent is Called "Gradient" Descent?

Because:

* gradient = slope
* descent = moving downward

---

## Why Learning Rate is Important?

Too small:

* slow learning

Too large:

* unstable learning

---

## Why Gradient Descent is Important?

Because it helps machine learning models learn optimal weights.

---

# Final Summary

| Concept          | Meaning                |
| ---------------- | ---------------------- |
| Gradient Descent | Optimization algorithm |
| Goal             | Minimize loss/error    |
| Gradient         | Slope/direction        |
| Learning Rate    | Step size              |
| Batch GD         | Uses full dataset      |
| SGD              | Uses one sample        |
| Mini-Batch GD    | Uses small batches     |
| Adam             | Advanced optimizer     |