# Bias vs Variance

Bias and Variance are two major sources of error in machine learning models.

They help explain:

* underfitting
* overfitting
* model performance

---

# Simple Idea

```python id="jlwm1v"
Bias  -> Model too simple
Variance -> Model too complex
```

---

# 1. Bias

Bias means:

```python id="jlwm2w"
Model makes strong assumptions and fails to learn patterns properly
```

High bias causes:

* underfitting
* poor training performance
* poor testing performance

---

# High Bias Example

Suppose actual relationship is:

```python id="jlwm3x"
y = x²
```

But model uses:

```python id="jlwm4y"
y = mx + c
```

Linear model cannot capture curve properly.

This is high bias.

---

# Signs of High Bias

| Sign                  | Meaning               |
| --------------------- | --------------------- |
| Low training accuracy | Model too simple      |
| Low test accuracy     | Cannot learn patterns |
| Underfitting          | High bias problem     |

---

# 2. Variance

Variance means:

```python id="jlwm5z"
Model learns training data too closely including noise
```

High variance causes:

* overfitting
* excellent training accuracy
* poor testing accuracy

---

# High Variance Example

Suppose model memorizes:

* every training point
* random noise

Training:

```python id="jlwm6a"
99% accuracy
```

Testing:

```python id="jlwm7b"
60% accuracy
```

This is high variance.

---

# Signs of High Variance

| Sign                        | Meaning               |
| --------------------------- | --------------------- |
| Very high training accuracy | Model memorizing      |
| Poor test accuracy          | Cannot generalize     |
| Overfitting                 | High variance problem |

---

# Visual Understanding

## High Bias

```python id="jlwm8c"
Simple model
Misses patterns
```

---

## High Variance

```python id="jlwm9d"
Very complex model
Memorizes data
```

---

## Balanced Model

```python id="jlwm0e"
Learns actual patterns
Generalizes well
```

---

# Bias-Variance Tradeoff

Important rule:

```python id="jlwm1f"
Reducing bias often increases variance
Reducing variance often increases bias
```

Goal:

* find balance

---

# Example

| Model              | Bias     | Variance |
| ------------------ | -------- | -------- |
| Linear Regression  | High     | Low      |
| Deep Decision Tree | Low      | High     |
| Random Forest      | Balanced | Moderate |

---

# Real Life Analogy

# High Bias

Student studies very little.

Result:

* poor in all exams

---

# High Variance

Student memorizes exact questions.

Result:

* fails when questions change

---

# Balanced Learning

Student understands concepts properly.

Best performance.

---

# How to Reduce High Bias

* Use more complex model
* Add more features
* Reduce regularization
* Train longer

---

# How to Reduce High Variance

* Use regularization
* Reduce model complexity
* Add more training data
* Use dropout/pruning

---

# Connection with Regularization

| Method         | Effect          |
| -------------- | --------------- |
| Ridge/Lasso    | Reduce variance |
| Complex models | Reduce bias     |
| Simpler models | Reduce variance |

---

# Machine Learning Example

## High Bias

```python id="jlwm2g"
Train Accuracy = 65%
Test Accuracy = 60%
```

Model too simple.

---

## High Variance

```python id="jlwm3h"
Train Accuracy = 99%
Test Accuracy = 70%
```

Model overfitting.

---

## Balanced

```python id="jlwm4i"
Train Accuracy = 91%
Test Accuracy = 89%
```

Good generalization.

---

# Interview Definition

```python id="jlwm5j"
Bias is error due to overly simple assumptions, while variance is error due to excessive sensitivity to training data.
```

---

# Final Summary

| Concept       | Meaning                |
| ------------- | ---------------------- |
| Bias          | Model too simple       |
| Variance      | Model too complex      |
| High Bias     | Underfitting           |
| High Variance | Overfitting            |
| Goal          | Balance both           |
| Solution      | Bias-Variance Tradeoff |
