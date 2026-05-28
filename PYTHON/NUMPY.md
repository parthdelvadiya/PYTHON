# NumPy Important Methods with Examples

# What is NumPy?

NumPy is a Python library used for:

* Numerical Computing
* Arrays
* Matrix Operations
* Fast Mathematical Calculations

Import NumPy:

```python id="x4h3mz"
import numpy as np
```

---

# Creating Arrays

---

# 1D Array

```python id="1q3fva"
arr = np.array([1, 2, 3, 4])

print(arr)
```

Output:

```python id="2h4zcl"
[1 2 3 4]
```

---

# 2D Array

```python id="31b9l0"
arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr)
```

---

# Array Properties

---

# ndim

Returns dimensions.

```python id="bq6ttn"
arr.ndim
```

Output:

```python id="gk0e7n"
2
```

---

# shape

Returns rows and columns.

```python id="v0o7v8"
arr.shape
```

Output:

```python id="mj6pqa"
(2, 2)
```

---

# size

Returns total elements.

```python id="8tq6h9"
arr.size
```

---

# dtype

Returns datatype.

```python id="8c52e5"
arr.dtype
```

---

# Changing Datatype

```python id="4d5txm"
arr.astype(float)
```

---

# Special Arrays

---

# zeros()

Creates array of zeros.

```python id="l1o2fc"
np.zeros((2, 3))
```

Output:

```python id="g8i2v4"
[[0. 0. 0.]
 [0. 0. 0.]]
```

---

# ones()

Creates array of ones.

```python id="r3s4fz"
np.ones((2, 2))
```

---

# full()

Creates array with fixed value.

```python id="v9f7qb"
np.full((2,2), 5)
```

---

# eye()

Identity matrix.

```python id="v6d3kc"
np.eye(3)
```

---

# arange()

Works like range().

```python id="6z4f8h"
np.arange(1, 10, 2)
```

Output:

```python id="i8g9yz"
[1 3 5 7 9]
```

---

# linspace()

Equal spaced values.

```python id="7h5m9u"
np.linspace(0, 10, 5)
```

---

# Random Methods

---

# random.rand()

Random numbers between 0 and 1.

```python id="s1v4tk"
np.random.rand(2, 2)
```

---

# random.randint()

Random integers.

```python id="g9m4yf"
np.random.randint(1, 10, size=(2,2))
```

---

# random.seed()

Fix random values.

```python id="4n2p5j"
np.random.seed(42)
```

---

# Array Indexing

---

# Access Element

```python id="e5x6dr"
arr[0]
```

---

# 2D Access

```python id="8y4qna"
arr[0, 1]
```

---

# Slicing

```python id="s0d8fg"
arr[1:4]
```

---

# 2D Slicing

```python id="5q8mkt"
arr[:, 0]
```

Meaning:

* `:` → all rows
* `0` → first column

---

# Reshaping Arrays

---

# reshape()

Changes shape.

```python id="9h1zvt"
arr = np.array([1,2,3,4,5,6])

arr.reshape(2,3)
```

---

# flatten()

Converts to 1D.

```python id="u8d1ol"
arr.flatten()
```

---

# Mathematical Operations

---

# Addition

```python id="h7g4cp"
a + b
```

---

# Subtraction

```python id="p4v8mi"
a - b
```

---

# Multiplication

```python id="l3k9xr"
a * b
```

---

# Division

```python id="r0w5tb"
a / b
```

---

# Power

```python id="t8c1yv"
a ** 2
```

---

# Aggregate Functions

---

# sum()

```python id="6d4xqn"
arr.sum()
```

---

# mean()

```python id="j5f9ow"
arr.mean()
```

---

# max()

```python id="g2p7dx"
arr.max()
```

---

# min()

```python id="d4q1yk"
arr.min()
```

---

# std()

Standard deviation.

```python id="z6x4ev"
arr.std()
```

---

# axis Concept

---

## axis=0 → Column Wise

```python id="l9v2bn"
arr.sum(axis=0)
```

---

## axis=1 → Row Wise

```python id="h0w3pz"
arr.sum(axis=1)
```

---

# Boolean Masking

Filtering arrays using conditions.

```python id="5r1xkc"
arr[arr > 5]
```

---

# Copy vs View

---

# copy()

Independent copy.

```python id="z9f7tm"
b = arr.copy()
```

---

# view()

Shares memory.

```python id="s8n5xy"
b = arr.view()
```

---

# Joining Arrays

---

# concatenate()

```python id="v3y5mw"
np.concatenate((a, b))
```

---

# vstack()

Vertical stack.

```python id="h7d4ua"
np.vstack((a, b))
```

---

# hstack()

Horizontal stack.

```python id="r4j8zx"
np.hstack((a, b))
```

---

# Splitting Arrays

---

# split()

```python id="n2t8qy"
np.split(arr, 2)
```

---

# Sorting Arrays

---

# sort()

```python id="d5g8pr"
np.sort(arr)
```

---

# Searching

---

# where()

Returns indexes.

```python id="x6h2fm"
np.where(arr > 5)
```

---

# unique()

Unique values.

```python id="s1z9wr"
np.unique(arr)
```

---

# Matrix Operations

---

# Matrix Multiplication

```python id="y4w7pt"
np.dot(a, b)
```

or

```python id="v8k3xs"
a @ b
```

---

# Transpose Matrix

```python id="l7d2ny"
arr.T
```

---

# Determinant

```python id="i3q8zm"
np.linalg.det(arr)
```

---

# Inverse Matrix

```python id="r6t1vx"
np.linalg.inv(arr)
```

---

# Eigen Values

```python id="u9w5cz"
np.linalg.eig(arr)
```

---

# Broadcasting

NumPy automatically adjusts shapes.

```python id="k1g9mu"
arr + 5
```

Adds 5 to every element.

---

# Important Interview Notes

| Method        | Purpose               |
| ------------- | --------------------- |
| array()       | Create array          |
| reshape()     | Change shape          |
| flatten()     | Convert to 1D         |
| arange()      | Range array           |
| linspace()    | Equal intervals       |
| sum()         | Total                 |
| mean()        | Average               |
| concatenate() | Join arrays           |
| where()       | Conditional search    |
| dot()         | Matrix multiplication |

---

# NumPy vs Python List

| NumPy Array           | Python List     |
| --------------------- | --------------- |
| Faster                | Slower          |
| Less memory           | More memory     |
| Vectorized operations | Manual loops    |
| Numerical computing   | General purpose |

---

# Most Common NumPy Workflow

```python id="d5m8ru"
import numpy as np

arr = np.array([1,2,3,4,5])

print(arr.mean())

print(arr.max())

new_arr = arr * 2

print(new_arr)
```

Output:

```python id="k7p2xq"
3.0
5
[2 4 6 8 10]
```

---
