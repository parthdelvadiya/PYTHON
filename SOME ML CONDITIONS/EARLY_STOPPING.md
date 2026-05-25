# Early Stopping

Early Stopping is a regularization technique used to prevent overfitting during training.

It stops training when model performance on validation data stops improving.

---

# Simple Definition

```python id="jlwm1a"
Early stopping stops training before the model starts overfitting.
```

---

# Why Early Stopping is Needed

During training:

* training accuracy keeps increasing
* but validation accuracy may start decreasing

This means:

* model is memorizing training data
* overfitting has started

Early stopping prevents this.

---

# Simple Understanding

Suppose:

```python id="jlwm2b"
Epoch 1  -> Validation Loss = 0.8
Epoch 5  -> Validation Loss = 0.3
Epoch 10 -> Validation Loss = 0.2
Epoch 20 -> Validation Loss = 0.5
```

After epoch 10:

* validation performance becomes worse

Best model was at:

* epoch 10

Early stopping stops training there.

---

# Important Terms

| Term            | Meaning                         |
| --------------- | ------------------------------- |
| Epoch           | One full training cycle         |
| Training Loss   | Error on training data          |
| Validation Loss | Error on unseen validation data |

---

# Visual Understanding

```text id="jlwm3c"
Training Loss     ↓ continuously
Validation Loss   ↓ then ↑

When validation loss increases:
Overfitting starts
```

---

# How Early Stopping Works

Steps:

1. Train model
2. Monitor validation performance
3. Check if performance improves
4. Stop training when improvement stops

---

# Patience Parameter

Patience means:

```python id="jlwm4d"
How many epochs to wait before stopping
```

Example:

```python id="jlwm5e"
patience = 3
```

If validation loss does not improve for 3 epochs:

* training stops

---

# TensorFlow Example

```python id="jlwm6f"
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3
)
```

---

# Model Training

```python id="jlwm7g"
model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    callbacks=[early_stop]
)
```

---

# PyTorch Concept

In PyTorch:

* manually monitor validation loss
* stop training when performance worsens

---

# Why Early Stopping is Important

Benefits:

* reduces overfitting
* saves training time
* improves generalization
* avoids unnecessary epochs

---

# Real Life Analogy

Suppose student studies for exam.

Initially:

* understanding improves

After too much repetition:

* memorization starts
* efficiency decreases

Best point is before over-memorization.

This is early stopping.

---

# Early Stopping vs Regularization

| Method         | Purpose                |
| -------------- | ---------------------- |
| Early Stopping | Stop over-training     |
| Ridge/Lasso    | Penalize weights       |
| Dropout        | Disable random neurons |

All help reduce overfitting.

---

# Example

Without Early Stopping:

```python id="jlwm8h"
Train Accuracy = 99%
Validation Accuracy = 70%
```

Overfitting.

---

# With Early Stopping

```python id="jlwm9i"
Train Accuracy = 92%
Validation Accuracy = 89%
```

Better generalization.

---

# Common Monitoring Metrics

| Metric       | Used For             |
| ------------ | -------------------- |
| val_loss     | Most common          |
| val_accuracy | Classification tasks |

---

# Best Practice

Usually monitor:

```python id="jlwm0j"
validation loss
```

Because:

* accuracy can fluctuate
* loss gives smoother signal

---

# Interview Definition

```python id="jlwm1k"
Early stopping is a regularization technique that stops model training when validation performance stops improving, helping prevent overfitting.
```

---

# Final Summary

| Concept        | Meaning                            |
| -------------- | ---------------------------------- |
| Early Stopping | Stop training before overfitting   |
| Main Goal      | Better generalization              |
| Monitors       | Validation performance             |
| Patience       | Waiting epochs before stop         |
| Benefit        | Reduces overfitting and saves time |