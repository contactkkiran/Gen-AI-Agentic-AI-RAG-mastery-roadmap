from re import A
from statistics import linear_regression

from sklearn.linear_model import LinearRegression
import numpy as np

# Step 1: Training data
X = np.array([[1], [2], [3], [4]])  # Feature (hours studied)
Y = np.array([2, 4, 6, 8])  # Label (marks scored)

# Step 2: Create model
model = LinearRegression()

# Step 3: Train model
model.fit(X, Y)

# Step 4: Predict
prediction = model.predict(np.array([[5]]))

print(prediction)


# Create training data where y = 3x + 2.
# • Train a LinearRegression model.
# • Predict the value of y when x = 10.


x = np.array([[1], [2], [3], [4], [5]])
y = np.array([5, 8, 11, 14, 17])
model = LinearRegression()

# Training model
model.fit(x, y)

# predict
prediction = model.predict(np.array([[10]]))
print(prediction)


#  Create training data where y = 4 x + 2.
# # • Train a LinearRegression model.
# # • Predict the value of y when x = 10.

a = np.array([[1], [2], [3], [4], [5]])
b = [6, 10, 14, 18, 22]

# Trainig model
model.fit(a, b)
prediction = model.predict(np.array([[10]]))
print(prediction)

# Quiz 1
# Using the equation above (y = 7x + 5):
# Write the complete code to:

# 1. Import LinearRegression
# 2. Create X
# 3. Create y
# 4. Create the model
# 5. Train the model
# 6. Predict for x = 20

x = np.array([[1], [2], [3], [4], [5]])
y = [12, 19, 26, 29, 40]

# train
model.fit(x, y)
# predict
predction = model.predict(np.array([[20]]))
print(predction)

print(model.coef_)  # What slope did the model learn?
print(model.intercept_)  # What intercept did the model learn?

# Quiz 3 - Spot the Bug

# What’s wrong with this code?

from sklearn.linear_model import LinearRegression

# X = [[1], [2], [3]]
# y = [5, 8]

# model = LinearRegression()
# model.fit(X, y)

# 🟡 Quiz 4 - Predict Without Python

# Calculate: y = 9x - 4

# * model.predict([[10]]) = ?
# * model.predict([[25]]) = ?
# * model.predict([[100]]) = ?
# solution
# 86
# 225
# 885
