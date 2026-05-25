# Sampling Bias

Sampling Bias happens when the training data does not properly represent real-world data.

Because of this:

* model learns wrong patterns
* predictions become biased
* real-world accuracy decreases

---

# Simple Example

Suppose you want to survey:

```python id="lhg0sj"
"Do students like online classes?"
```

But you only ask:

* Computer Science students

You ignore:

* Civil
* Mechanical
* Electrical students

Result:

* biased survey

---

# Machine Learning Example

Dataset:

```python id="djlwm1"
95% Normal Transactions
5% Fraud Transactions
```

Model learns:

```python id="jlwm2q"
"Everything is normal"
```

Accuracy may become:

```python id="jlwm3w"
95%
```

But fraud detection becomes poor.

---

# Common Types

| Type               | Example                            |
| ------------------ | ---------------------------------- |
| Selection Bias     | Data collected from one group only |
| Survivorship Bias  | Only successful cases considered   |
| Undercoverage Bias | Some groups missing completely     |
| Non-response Bias  | Only certain people respond        |

---

# Real AI Example

Face recognition trained mostly on:

* light skin faces

May perform poorly on:

* dark skin faces

This is sampling bias.

---

# How to Reduce Sampling Bias

* Collect diverse data
* Use random sampling
* Balance classes
* Use stratified sampling

---

# Python Example

```python id="jlwm4e"
from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler()

X_resampled, y_resampled = ros.fit_resample(X, y)
```

Used to balance dataset classes.

---

# Sampling Bias vs Overfitting

| Concept       | Meaning                       |
| ------------- | ----------------------------- |
| Sampling Bias | Bad/unrepresentative data     |
| Overfitting   | Model memorizes training data |

---

# Final Summary

| Concept       | Meaning                               |
| ------------- | ------------------------------------- |
| Sampling Bias | Dataset does not represent real world |
| Main Problem  | Biased predictions                    |
| Common Cause  | Imbalanced or limited data            |
| Solution      | Balanced and diverse dataset          |