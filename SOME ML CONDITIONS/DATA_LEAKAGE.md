# Data Leakage

Data Leakage happens when the model gets information during training that it should not normally have.

Because of this:

* model performs unrealistically well
* training accuracy becomes very high
* real-world performance becomes poor

---

# Simple Definition

```python id="jlwm1a"
Data leakage occurs when future or hidden information leaks into training data.
```

---

# Easy Example

Suppose you want to predict:

```python id="jlwm2b"
"Will student pass exam?"
```

Features:

* study_hours
* attendance
* final_result

Problem:

```python id="jlwm3c"
final_result = Pass/Fail
```

You already gave the answer to the model.

This is data leakage.

---

# Machine Learning Example

Suppose predicting loan approval.

Features:

```python id="jlwm4d"
salary
credit_score
loan_status
```

Target:

```python id="jlwm5e"
loan_status
```

If `loan_status` is accidentally included in input features,
the model cheats.

---

# Why Data Leakage is Dangerous

Model learns:

```python id="jlwm6f"
Hidden answers instead of real patterns
```

Result:

* extremely high training accuracy
* terrible real-world performance

---

# Common Signs of Data Leakage

| Sign                            | Meaning                  |
| ------------------------------- | ------------------------ |
| Unrealistically high accuracy   | Leakage possible         |
| Validation accuracy too perfect | Model may be cheating    |
| Sudden huge improvement         | Check features carefully |

---

# Types of Data Leakage

# 1. Target Leakage

Target-related information leaks into features.

Example:

```python id="jlwm7g"
Using final exam marks to predict pass/fail
```

---

# 2. Train-Test Leakage

Test data accidentally enters training data.

Example:

```python id="jlwm8h"
Scaling entire dataset before train-test split
```

Wrong:

```python id="jlwm9i"
Scaler learns information from test data
```

---

# Wrong Example

```python id="jlwm0j"
# WRONG

scaler.fit(X)

X_train, X_test = train_test_split(X)
```

---

# Correct Example

```python id="jlwm1k"
# CORRECT

X_train, X_test = train_test_split(X)

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

---

# Real Life Analogy

Suppose teacher gives:

* exam questions before exam

Student scores very high.

But actual knowledge is low.

This is data leakage.

---

# Real AI Example

Suppose medical AI predicts disease.

Dataset accidentally contains:

```python id="jlwm2l"
medicine_given_after_diagnosis
```

But medicine is only given after disease confirmation.

Model cheats using future information.

---

# How to Prevent Data Leakage

* Split train/test early
* Never use future information
* Remove target-related columns
* Perform preprocessing after split
* Carefully inspect features

---

# Data Leakage vs Overfitting

| Concept      | Meaning                              |
| ------------ | ------------------------------------ |
| Data Leakage | Model gets hidden/future information |
| Overfitting  | Model memorizes training patterns    |

---

# Interview Definition

```python id="jlwm3m"
Data leakage occurs when information unavailable during real-world prediction accidentally enters the training process, causing unrealistically high model performance.
```

---

# Final Summary

| Concept      | Meaning                                   |
| ------------ | ----------------------------------------- |
| Data Leakage | Hidden/future information enters training |
| Main Problem | Model cheats                              |
| Result       | Fake high accuracy                        |
| Common Cause | Bad preprocessing or wrong features       |
| Solution     | Proper train-test separation              |
