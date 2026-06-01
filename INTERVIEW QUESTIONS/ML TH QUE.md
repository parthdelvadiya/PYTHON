# AI/ML Interview Questions and Answers

---

# 1. What is the difference between AI, Machine Learning, and Deep Learning?

## Answer

- Artificial Intelligence (AI) is the broad field of creating systems that can perform tasks requiring human intelligence.
- Machine Learning (ML) is a subset of AI where models learn patterns from data.
- Deep Learning (DL) is a subset of ML that uses neural networks with multiple layers.

### Example

- AI → Self-driving cars
- ML → House price prediction
- DL → Face recognition, image generation, ChatGPT

---

# 2. What is Overfitting?

## Answer

Overfitting occurs when a model learns the training data too well, including noise and unnecessary details.

### Symptoms

- High training accuracy
- Low testing accuracy

### Solutions

- More data
- Regularization
- Cross Validation
- Data Augmentation
- Simpler model

---

# 3. What is Underfitting?

## Answer

Underfitting happens when a model is too simple and cannot capture patterns in data.

### Symptoms

- Low training accuracy
- Low testing accuracy

### Solutions

- Increase model complexity
- Add useful features
- Reduce regularization

---

# 4. What is the Bias-Variance Tradeoff?

## Answer

### High Bias

Model is too simple and misses patterns.

### High Variance

Model is too complex and memorizes data.

### Goal

Build a model with:

- Low Bias
- Low Variance

---

# 5. Why do we split data into Train, Validation, and Test Sets?

## Answer

### Training Set

Used to train the model.

### Validation Set

Used for hyperparameter tuning.

### Test Set

Used for final evaluation.

### Example

- Train → 70%
- Validation → 15%
- Test → 15%

---

# 6. What is Cross Validation?

## Answer

Cross Validation evaluates model performance using multiple train-test splits.

### Example

5-Fold Cross Validation

- Fold 1 → Test
- Remaining → Train

Repeat for all folds and average the results.

### Benefits

- More reliable evaluation
- Better use of limited data

---

# 7. What is Data Leakage?

## Answer

Data Leakage occurs when information unavailable in real-world predictions is accidentally included during training.

### Example

Predicting student performance using:

- Attendance
- Assignment Marks
- Final Result

Using "Final Result" as a feature causes leakage.

---

# 8. What is Class Imbalance?

## Answer

Class imbalance occurs when one class has significantly more samples than another.

### Example

- Normal Transactions → 9900
- Fraud Transactions → 100

A model predicting all transactions as normal achieves 99% accuracy but is useless.

### Solutions

- Oversampling
- Undersampling
- SMOTE
- Class Weights

---

# 9. Why is Accuracy Not Always a Good Metric?

## Answer

Accuracy can be misleading for imbalanced datasets.

### Example

- Healthy → 990
- Disease → 10

Predicting everyone as healthy:

Accuracy = 99%

But the model misses all disease cases.

### Better Metrics

- Precision
- Recall
- F1 Score
- ROC-AUC

---

# 10. Difference Between Precision and Recall

## Answer

### Precision

Measures how many predicted positives are actually positive.

Formula:

Precision = TP / (TP + FP)

### Recall

Measures how many actual positives are correctly identified.

Formula:

Recall = TP / (TP + FN)

### Example

For disease detection, Recall is usually more important.

---

# 11. What is F1 Score?

## Answer

F1 Score balances Precision and Recall.

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

### Use Case

Useful when dealing with imbalanced datasets.

---

# 12. What is Feature Engineering?

## Answer

Feature Engineering involves creating new useful features from existing data.

### Example

Original Feature:

- Date of Birth

Generated Features:

- Age
- Age Group
- Years Until Retirement

Better features often improve performance significantly.

---

# 13. What is Feature Selection?

## Answer

Feature Selection means choosing important features and removing irrelevant ones.

### Benefits

- Faster training
- Reduced overfitting
- Better interpretability

### Methods

- Correlation Analysis
- Recursive Feature Elimination (RFE)
- Lasso Regression
- Feature Importance

---

# 14. What is Multicollinearity?

## Answer

Multicollinearity occurs when multiple features are highly correlated.

### Example

- Age
- Birth Year

Both contain similar information.

### Problems

- Unstable coefficients
- Difficult interpretation

### Solutions

- Remove correlated features
- PCA
- VIF Analysis

---

# 15. Why Do We Normalize or Standardize Data?

## Answer

Many algorithms perform better when features are on similar scales.

### Example

- Salary = 100000
- Age = 25

Salary dominates calculations.

### Standardization Formula

z = (x - μ) / σ

### Algorithms That Need Scaling

- KNN
- SVM
- Logistic Regression
- Neural Networks

---

# 16. Why Does KNN Require Scaling?

## Answer

KNN uses distance calculations.

Without scaling, larger numerical values dominate the distance metric.

### Example

- Salary = 100000
- Age = 25

Salary heavily influences distance calculations.

Scaling ensures fair contribution from all features.

---

# 17. Why Are Decision Trees Not Affected by Scaling?

## Answer

Decision Trees split data based on conditions.

Example:

salary > 50000

Since they do not rely on distance calculations, scaling generally has no effect.

---

# 18. Random Forest vs Decision Tree

## Answer

### Decision Tree

Advantages:

- Easy to understand
- Fast

Disadvantages:

- Prone to overfitting

### Random Forest

Advantages:

- Better accuracy
- Less overfitting

Disadvantages:

- Harder to interpret

---

# 19. Explain Bagging and Boosting

## Answer

### Bagging

Models are trained independently.

Example:

- Random Forest

Goal:

- Reduce Variance

### Boosting

Models are trained sequentially.

Each model learns from previous mistakes.

Examples:

- AdaBoost
- XGBoost
- LightGBM

Goal:

- Reduce Bias

---

# 20. What is Gradient Descent?

## Answer

Gradient Descent is an optimization algorithm used to minimize loss.

### Steps

1. Calculate loss
2. Compute gradient
3. Update weights
4. Repeat

### Used In

- Linear Regression
- Logistic Regression
- Neural Networks

---

# 21. What is the Vanishing Gradient Problem?

## Answer

Gradients become extremely small during backpropagation.

### Result

Earlier layers stop learning effectively.

### Solutions

- ReLU Activation
- Batch Normalization
- Residual Connections (ResNet)

---

# 22. What is Dropout?

## Answer

Dropout is a regularization technique used to prevent overfitting.

### Example

Dropout = 0.5

Randomly disables 50% of neurons during training.

### Benefits

- Better generalization
- Reduced overfitting

---

# 23. How Would You Handle Missing Values?

## Answer

Common approaches:

- Drop Rows
- Drop Columns
- Mean Imputation
- Median Imputation
- Mode Imputation
- KNN Imputation

Choice depends on the dataset and business requirements.

---

# 24. What Would You Do If Model Accuracy Suddenly Drops After Deployment?

## Answer

Investigate:

- Data Drift
- Model Drift
- Data Quality Issues
- Pipeline Failures
- Feature Changes

### Actions

- Monitor performance
- Retrain model
- Update features

---

# 25. Explain an End-to-End ML Pipeline

## Answer

```text
Data Collection
      ↓
Data Cleaning
      ↓
EDA
      ↓
Feature Engineering
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Hyperparameter Tuning
      ↓
Evaluation
      ↓
Deployment
      ↓
Monitoring
      ↓
Retraining
```

### Purpose

Ensures the complete lifecycle of an ML model from raw data to production.

---

# Final Interview Tip

When answering AI/ML interview questions:

1. Define the concept.
2. Explain why it matters.
3. Give a real-world example.
4. Mention advantages and limitations.
5. Discuss practical use cases.

This approach makes answers sound much stronger during interviews.