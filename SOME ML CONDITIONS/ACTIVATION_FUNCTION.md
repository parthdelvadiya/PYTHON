# Activation Functions in Deep Learning

Activation Functions help Neural Networks learn complex patterns by introducing non-linearity.

Without activation functions:

```python
Neural Network = Linear Model
```

No matter how many layers are added, the network behaves like a simple linear equation.

---

# Why Activation Functions Are Needed

Suppose we want to learn:

```python
Image Classification
Speech Recognition
Fraud Detection
Object Detection
```

These problems contain complex non-linear relationships.

Activation functions allow Neural Networks to learn those relationships.

---

# Simple Workflow

```python
Input
   ↓
Weighted Sum
   ↓
Activation Function
   ↓
Output
```

Formula:

```python
Output = Activation(WX + B)
```

Where:

* W = Weights
* X = Inputs
* B = Bias
* Activation = Activation Function

---

# Types of Activation Functions

1. Binary Step
2. Linear
3. Sigmoid
4. Tanh
5. ReLU
6. Leaky ReLU
7. PReLU
8. ELU
9. SELU
10. Softplus
11. Swish
12. GELU
13. Softmax

---

# 1. Binary Step Function

Produces only:

```python
0 or 1
```

Rule:

```python
x >= 0 → 1
x < 0  → 0
```

### Example

```python
Input = 5
Output = 1
```

```python
Input = -2
Output = 0
```

### Advantages

* Simple
* Fast

### Disadvantages

* Not differentiable
* Cannot be used effectively in modern neural networks

### Best Use

```python
Perceptron
Basic Logic Gates
```

---

# 2. Linear Activation

Output equals input.

Formula:


::contentReference[oaicite:0]{index=0}


### Example

```python
Input = 10
Output = 10
```

### Problem

Multiple layers still behave linearly.

### Best Use

```python
Regression Output Layer
```

---

# 3. Sigmoid Function

Output range:

```python
0 to 1
```

Formula:


::contentReference[oaicite:1]{index=1}


### Example

```python
Input = 0
Output = 0.5
```

### Advantages

* Probability interpretation
* Smooth curve

### Disadvantages

* Vanishing Gradient Problem
* Slow training

### Best Use

```python
Binary Classification Output Layer
```

---

# 4. Tanh Function

Output range:

```python
-1 to 1
```

Formula:


::contentReference[oaicite:2]{index=2}


### Example

```python
Input = 0
Output = 0
```

### Advantages

* Zero-centered output
* Better than Sigmoid

### Disadvantages

* Vanishing Gradient Problem

### Best Use

```python
Hidden Layers (Older Networks)
```

---

# 5. ReLU (Rectified Linear Unit)

Most popular activation function.

Rule:

```python
x > 0 → x
x <= 0 → 0
```

Formula:

:contentReference[oaicite:3]{index=3}

### Example

```python
Input = 5
Output = 5
```

```python
Input = -3
Output = 0
```

### Advantages

* Fast
* Simple
* Solves Vanishing Gradient partially

### Disadvantages

* Dying ReLU Problem

### Best Use

```python
Hidden Layers
CNN
ANN
```

---

# 6. Leaky ReLU

Improved version of ReLU.

Rule:

```python
x > 0 → x
x <= 0 → 0.01x
```

Formula:

:contentReference[oaicite:4]{index=4}

### Advantages

* Prevents Dying ReLU

### Best Use

```python
Deep Neural Networks
CNN
```

---

# 7. PReLU

Parametric ReLU.

Rule:

```python
x > 0 → x
x <= 0 → αx
```

Where:

```python
α is learned automatically
```

### Advantage

Network learns the best negative slope.

---

# 8. ELU

Full Form:

```python
Exponential Linear Unit
```

Formula:

```python
x                     if x > 0
α(e^x − 1)            if x <= 0
```

### Advantages

* Reduces bias shift
* Better learning

### Best Use

```python
Deep Networks
```

---

# 9. SELU

Full Form:

```python
Scaled Exponential Linear Unit
```

Improved version of ELU.

### Advantages

* Self-normalizing
* Stable training

### Best Use

```python
Very Deep Networks
```

---

# 10. Softplus

Smooth version of ReLU.

Formula:


::contentReference[oaicite:5]{index=5}


### Advantages

* Differentiable everywhere
* No sharp corners

### Disadvantages

* Slower than ReLU

---

# 11. Swish

Developed by :contentReference[oaicite:6]{index=6}.

Formula:


::contentReference[oaicite:7]{index=7}


### Advantages

* Often outperforms ReLU
* Smooth gradients

### Best Use

```python
Modern Deep Learning Models
```

---

# 12. GELU

Full Form:

```python
Gaussian Error Linear Unit
```

Used heavily in:

* :contentReference[oaicite:8]{index=8}
* :contentReference[oaicite:9]{index=9}
* Transformer Models

### Advantages

* Excellent performance
* Smooth activation

### Best Use

```python
NLP
Transformers
Large Language Models
```

---

# 13. Softmax

Used for Multi-Class Classification.

Formula:

:contentReference[oaicite:10]{index=10}

### Example

Before Softmax:

```python
[2.5, 1.2, 0.8]
```

After Softmax:

```python
[0.68, 0.20, 0.12]
```

Probabilities sum to:

```python
1
```

### Best Use

```python
Multi-Class Classification
```

---

# Activation Function Selection

| Problem Type | Activation Function |
|-------------|--------------------|
| Hidden Layers | ReLU |
| Deep Networks | Leaky ReLU |
| Binary Classification | Sigmoid |
| Multi-Class Classification | Softmax |
| Regression | Linear |
| NLP Models | GELU |
| Modern CNNs | ReLU / Swish |

---

# Most Common Choices Today

### Hidden Layers

```python
ReLU
```

### Binary Classification Output

```python
Sigmoid
```

### Multi-Class Classification Output

```python
Softmax
```

### Transformers

```python
GELU
```

---

# Simple Analogy

Think of activation functions as decision makers.

Without activation:

```python
Input → Output
```

With activation:

```python
Input
 ↓
Decision
 ↓
Output
```

The decision step allows neural networks to learn complex patterns.

---

# Final Summary

| Activation Function | Output Range | Common Use |
|--------------------|-------------|------------|
| Binary Step | 0 or 1 | Perceptron |
| Linear | (-∞,∞) | Regression |
| Sigmoid | (0,1) | Binary Classification |
| Tanh | (-1,1) | Hidden Layers |
| ReLU | [0,∞) | Most Hidden Layers |
| Leaky ReLU | (-∞,∞) | Deep Networks |
| PReLU | (-∞,∞) | Advanced Networks |
| ELU | (-α,∞) | Deep Learning |
| SELU | Self-Normalized | Very Deep Networks |
| Softplus | (0,∞) | Smooth ReLU |
| Swish | Smooth Nonlinear | Modern Models |
| GELU | Smooth Nonlinear | Transformers |
| Softmax | Probabilities | Multi-Class Output |
