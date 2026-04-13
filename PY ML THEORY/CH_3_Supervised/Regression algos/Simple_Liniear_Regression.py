# What is Linear Regression?
# Linear Regression is a supervised learning algorithm used to predict continuous values.

# Predict house price
# Predict salary
# Predict sales

# Types of Linear Regression
# 1. Simple Linear Regression
# One input feature 
# 
# y = mx + b
# x → the input (what you control or choose)
# y → the output (what you get)
# m = Slope, coefficient (weight)
# b = intercept (bias)
# 
# 2. Multiple Linear Regression
# Multiple features 
# 
# y = b + w1​x1 ​+ w2​x2 ​+...+ wn​xn
# ​

# | Symbol | Meaning                            |
# | ------ | ---------------------------------- |
# |   X    | Input data (independent variables) |
# |   y    | Output data (dependent variable)   |

# For Simple linear regression This will be ideal situation
# X → (n, 1)
# y → (n,)


# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==============================
# 2. Load Dataset
# ==============================
data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("Dataset Preview:\n", df.head())


# ==============================
# 3. Define Features and Target (SIMPLE LINEAR)
# ==============================
X = df[['MedInc']]   # ✅ Only ONE feature
y = df['target']


# ==============================
# 4. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(  #20% → Testing 80% → Training
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ==============================
# 5. Train Model
# ==============================
model = LinearRegression()
model.fit(X_train, y_train)


# ==============================
# 6. Model Coefficients
# ==============================
print("\nModel Coefficients (Weight):", model.coef_[0]) #m
print("Intercept (Bias):", model.intercept_) #c


# ==============================
# 7. Predictions
# ==============================
y_pred = model.predict(X_test)

print("\nSample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i]:.2f}, Actual: {y_test.iloc[i]:.2f}")


# ==============================
# 8. Evaluation Metrics
# ==============================
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation Metrics:")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)



# | Metric | Use                       |
# | ------ | ------------------------- |
# | MAE    | simple error              | “On average, how much is my model wrong?” (Mean Absolute Error)
# | MSE    | training optimization     | "Take error Square it Take average" (Mean Squared Error)
# | RMSE   | real-world interpretation | "Just square root of MSE" (Root Mean Squared Error)
# | R²     | model quality             | "How well your model explains the data" (Coefficient of Determination)

# “MAE treats all errors equally, but MSE highlights big errors strongly”

# | R² Value | Meaning            |
# | -------- | ------------------ |
# | 1        | Perfect prediction | 
# | 0        | Useless model      |
# | < 0      | Very bad model     |


# ==============================
# 9. Overfitting Check
# ==============================
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("\nModel Performance:")
print("Training Score:", train_score)
print("Testing Score :", test_score)


# ==============================
# 10. Visualization (VERY IMPORTANT)
# ==============================
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, label="Actual Data")
plt.plot(X_test, y_pred, label="Regression Line")
plt.xlabel("Median Income")
plt.ylabel("House Price")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()


# ==============================
# 11. Final Interpretation
# ==============================
if train_score > test_score:
    print("\nModel might be slightly overfitting.")
elif train_score < test_score:
    print("\nModel might be underfitting.")
else:
    print("\nModel is well balanced.")
    
# ML models are designed to always expect X in this format:
# X → (n_samples, n_features)
# SO ALWAYS X WILL BE IN 2D AND Y WILL BE IN 1D

# What if we DON’T use Train-Test Split?
# Model will perform VERY well (almost perfect)
# BUT this is fake performance
# Problem: Overfitting
# Model just memorizes data, not learns pattern.
# Like this model.fit(X, y)
# This uses 100% data for training

# What if test_size is too high?
# Less training data → weak model

# What if test_size is too low?
# Testing becomes unreliable

# What is random_state=42?
# Controls randomness of splitting
# Every run → different split

# Why 42?
# No special meaning
# Just a commonly used number (from programming culture)


# X_train, X_test, y_train, y_test
# | Variable | Shape               |
# | -------- | ------------------- |
# | X_train  | (n_train, features) |
# | X_test   | (n_test, features)  |
# | y_train  | (n_train,)          |
# | y_test   | (n_test,)           |

# model.fit(X_train, y_train)
# Model learns patterns

# model.predict(X_test)
# Model is tested on unseen data



#Interview ready  
# Simple Linear Regression is a supervised learning algorithm used to model the 
# relationship between one independent variable and one dependent variable by fitting a straight line.

# How does the model learn?
# The model learns by minimizing the difference between actual and predicted values using a 
# loss function like Mean Squared Error.

# Why do we use MSE instead of MAE?
# MSE is used because it penalizes larger errors more than smaller ones, making the model sensitive to 
# significant mistakes and easier to optimize mathematically.

# What is the role of slope (m)?
# The slope represents how much the dependent variable changes for a one-unit 
# increase in the independent variable.

# What is intercept (b)?
# It is the value of the target variable when the input feature is zero.

# What is overfitting in linear regression?
# Overfitting occurs when the model learns noise from training data and 
# performs poorly on unseen data.
# Rare in simple linear regression
# More common in complex models

# What is underfitting?
# Underfitting occurs when the model is too simple to capture the underlying pattern in the data.