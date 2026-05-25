# Survivorship Bias

Survivorship Bias happens when we only focus on successful cases and ignore failures.

Because of this:

* conclusions become misleading
* analysis becomes biased
* important failures are ignored

---

# Simple Definition

```python id="jlwm1n"
Survivorship bias occurs when failed or missing data is ignored during analysis.
```

---

# Famous Example

During World War II:

Engineers studied returning airplanes.

They saw bullet holes on:

* wings
* tail
* body

Initial idea:

```python id="jlwm2o"
"Add armor where bullet holes exist"
```

But statistician Abraham Wald said:

```python id="jlwm3p"
"These planes survived."
```

Missing data:

* planes that crashed

Real conclusion:

* armor should be added where surviving planes had NO bullet holes

Those areas were critical.

---

# Easy Real Life Example

Suppose you study:

```python id="jlwm4q"
"How to become rich"
```

And only observe:

* successful billionaires

You ignore:

* millions of failed businesses

Result:

* misleading conclusions

---

# Machine Learning Example

Suppose fraud detection dataset contains only:

* successful transactions

Failed or blocked fraud attempts are missing.

Model learns incomplete patterns.

This is survivorship bias.

---

# Startup Example

People often say:

```python id="jlwm5r"
"Dropout founders become successful"
```

Examples:

* Bill Gates
* Mark Zuckerberg

But thousands of dropout failures are ignored.

This is survivorship bias.

---

# Why Survivorship Bias is Dangerous

It creates:

```python id="jlwm6s"
False success patterns
```

Because failures are hidden from analysis.

---

# Common Signs

| Sign                          | Meaning                 |
| ----------------------------- | ----------------------- |
| Only successful examples used | Failures ignored        |
| Unrealistic conclusions       | Missing data possible   |
| "Success secrets" analysis    | Often survivorship bias |

---

# Real AI Example

Suppose hiring AI trained only on:

* employees who stayed long-term

It ignores:

* rejected applicants
* employees who left early

Model becomes biased.

---

# How to Avoid Survivorship Bias

* Include failed cases
* Analyze missing data
* Use complete datasets
* Question success-only patterns

---

# Survivorship Bias vs Sampling Bias

| Concept           | Meaning                            |
| ----------------- | ---------------------------------- |
| Survivorship Bias | Only successful cases considered   |
| Sampling Bias     | Dataset not representative overall |

---

# Simple Analogy

Suppose you ask:

```python id="jlwm7t"
"How to pass exams?"
```

And only interview toppers.

You ignore:

* average students
* failed students

Your analysis becomes incomplete.

---

# Interview Definition

```python id="jlwm8u"
Survivorship bias occurs when analysis focuses only on successful outcomes while ignoring failures, leading to misleading conclusions.
```

---

# Final Summary

| Concept           | Meaning                               |
| ----------------- | ------------------------------------- |
| Survivorship Bias | Ignoring failures in analysis         |
| Main Problem      | Misleading conclusions                |
| Cause             | Missing failed cases                  |
| Effect            | False success patterns                |
| Solution          | Include both success and failure data |