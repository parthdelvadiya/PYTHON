# Biases in Machine Learning & Data Science

Bias is a systematic error that causes a model, dataset, experiment, or decision-making process to produce inaccurate or unfair results.

---

# 1. Sampling Bias

Sampling Bias happens when the training data does not properly represent real-world data.

Because of this:

* model learns wrong patterns
* predictions become biased
* real-world accuracy decreases

---

# Simple Example

Suppose you want to survey:

```python
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

```python
95% Normal Transactions
5% Fraud Transactions
```

Model learns:

```python
"Everything is normal"
```

Accuracy:

```python
95%
```

Fraud detection becomes poor.

---

# Solution

* Random Sampling
* Stratified Sampling
* Balanced Dataset

---

# 2. Selection Bias

Selection Bias occurs when data is selected in a way that favors certain outcomes.

---

# Example

Suppose a company asks:

```python
"Are employees happy?"
```

Survey sent only to:

* top performers

Ignored:

* average employees
* unhappy employees

Results become misleading.

---

# ML Example

Training data collected only from:

```python
Urban Areas
```

Model performs poorly in:

```python
Rural Areas
```

---

# Solution

* Collect data from all groups
* Random selection

---

# 3. Survivorship Bias

Survivorship Bias happens when only successful cases are analyzed.

Failed cases are ignored.

---

# Example

Looking at:

```python
Top Billionaires
```

Conclusion:

```python
Drop out of college to become rich
```

Ignored:

* millions of failed dropouts

---

# ML Example

Analyze only:

```python
Successful Loan Applications
```

Ignore:

```python
Rejected Applications
```

Model becomes biased.

---

# Solution

Include:

* successful cases
* failed cases

---

# 4. Undercoverage Bias

Occurs when some groups are completely missing from data.

---

# Example

Online survey:

```python
Google Form
```

Only internet users respond.

Missing:

* elderly people
* people without internet

---

# ML Example

Face recognition trained mostly on:

```python
Adults
```

Missing:

```python
Children
```

Poor child recognition.

---

# Solution

Include all target populations.

---

# 5. Non-response Bias

Occurs when certain people do not respond.

---

# Example

1000 people receive survey.

Only:

```python
200 respond
```

Responders may have different opinions.

---

# ML Example

Customer feedback dataset contains only:

```python
Very Happy Customers
```

Unhappy customers never respond.

---

# Solution

Increase participation rates.

---

# 6. Confirmation Bias

Occurs when people only focus on information supporting their beliefs.

---

# Example

Person believes:

```python
Online learning is best
```

Only reads articles supporting online learning.

Ignores opposing evidence.

---

# ML Example

Data scientist expects:

```python
Feature A is important
```

Only tests Feature A.

Misses better features.

---

# Solution

Analyze all evidence objectively.

---

# 7. Measurement Bias

Occurs when collected data is inaccurate.

---

# Example

Broken weighing machine:

```python
Actual Weight = 70kg
Measured = 75kg
```

---

# ML Example

Incorrect sensor values.

Model learns wrong relationships.

---

# Solution

Use accurate instruments and validation.

---

# 8. Observer Bias

Occurs when researchers influence observations.

---

# Example

Teacher grading favorite students more positively.

---

# ML Example

Manual image labeling:

```python
Labeler prefers one class
```

Labels become biased.

---

# Solution

Blind evaluations.

---

# 9. Reporting Bias

Occurs when only certain results are reported.

---

# Example

Company publishes:

```python
Positive Reviews
```

Hides:

```python
Negative Reviews
```

---

# ML Example

Only successful experiments documented.

Failed experiments ignored.

---

# Solution

Report all outcomes.

---

# 10. Recall Bias

Occurs when people remember events incorrectly.

---

# Example

Survey:

```python
How many times did you exercise last year?
```

People may not remember accurately.

---

# ML Example

Medical datasets based on patient memory.

Can contain inaccurate information.

---

# Solution

Use recorded data whenever possible.

---

# 11. Historical Bias

Occurs when historical data already contains unfairness.

---

# Example

Past hiring data:

```python
Mostly hired men
```

Model learns:

```python
Men are preferred
```

---

# AI Example

Recruitment AI becomes discriminatory.

---

# Solution

Fairness auditing.

---

# 12. Automation Bias

Occurs when people trust AI too much.

---

# Example

GPS says:

```python
Turn Right
```

Driver follows despite road closure.

---

# AI Example

Doctor blindly trusts AI diagnosis.

---

# Solution

Human verification.

---

# 13. Algorithmic Bias

Occurs when algorithm creates unfair outcomes.

---

# Example

Loan Approval AI favors certain groups.

---

# Cause

* biased training data
* biased features

---

# Solution

Fairness testing and auditing.

---

# 14. Class Imbalance Bias

Occurs when one class dominates dataset.

---

# Example

Dataset:

```python
99% Cats
1% Dogs
```

Model predicts:

```python
Cat
```

Almost always.

---

# Solution

Oversampling

```python
from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler()

X_resampled, y_resampled = ros.fit_resample(X, y)
```

---

# 15. Cultural Bias

Occurs when system reflects one culture more than others.

---

# Example

Chatbot trained mainly on:

```python
US English
```

May misunderstand:

```python
Indian English
```

---

# Solution

Use multicultural datasets.

---

# 16. Gender Bias

Occurs when one gender is unfairly favored.

---

# Example

Hiring AI prefers:

```python
Male Candidates
```

Because historical data favored males.

---

# Solution

Balanced and fair training data.

---

# 17. Availability Bias

Occurs when decisions rely on easily remembered examples.

---

# Example

News reports many airplane crashes.

People think:

```python
Flying is very dangerous
```

Even though statistics show otherwise.

---

# Solution

Use actual data instead of memory.

---

# 18. Publication Bias

Occurs when positive findings are published more often.

---

# Example

100 studies conducted.

Published:

```python
20 positive studies
```

Unpublished:

```python
80 negative studies
```

Creates misleading conclusions.

---

# Solution

Publish all research outcomes.

---

# 19. Label Bias

Occurs when labels are incorrect.

---

# Example

Dog image labeled as:

```python
Cat
```

Model learns wrong patterns.

---

# Solution

Careful data annotation.

---

# 20. Data Leakage Bias

Occurs when future information enters training data.

---

# Example

Predicting exam result using:

```python
Final Grade
```

as an input feature.

Model gets unrealistically high accuracy.

---

# Solution

Proper train-test separation.

---

# Final Summary Table

| Bias Type | Main Problem |
|------------|-------------|
| Sampling Bias | Data not representative |
| Selection Bias | Wrong data selection |
| Survivorship Bias | Failures ignored |
| Undercoverage Bias | Some groups missing |
| Non-response Bias | Certain people don't respond |
| Confirmation Bias | Looking only for supporting evidence |
| Measurement Bias | Incorrect measurements |
| Observer Bias | Human influence on observations |
| Reporting Bias | Selective reporting |
| Recall Bias | Incorrect memory |
| Historical Bias | Past unfairness learned |
| Automation Bias | Blind trust in AI |
| Algorithmic Bias | Unfair model behavior |
| Class Imbalance Bias | One class dominates |
| Cultural Bias | One culture overrepresented |
| Gender Bias | Gender unfairness |
| Availability Bias | Easily remembered examples dominate |
| Publication Bias | Only positive results published |
| Label Bias | Wrong labels |
| Data Leakage Bias | Future information leaks into training |

---

# Most Important Biases for ML Interviews

1. Sampling Bias
2. Selection Bias
3. Class Imbalance Bias
4. Historical Bias
5. Algorithmic Bias
6. Data Leakage Bias
7. Label Bias
8. Measurement Bias
9. Survivorship Bias
10. Confirmation Bias

These are the biases most frequently asked in Data Science, Machine Learning, AI, and Analytics interviews.