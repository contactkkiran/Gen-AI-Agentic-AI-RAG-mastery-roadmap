#  example 2 : Create training data where y = 8 x + 2.
# # • Train a LinearRegression model.
# # • Predict the value of y when x = 10.
import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()
a = np.array([[1], [2], [3], [4], [5]])
b = [10, 18, 26, 34, 42]

# Trainig model
model.fit(a, b)
prediction = model.predict(np.array([[10]]))
print(prediction)

# inerception interception = y - mx
# Using the first row (x = 1, y = 10):
b = 10 - (8 * 1)

b = 10 - 8

b = 2
print("Interception :", b)


# Coding Questions (Very Common)
# Q1

# * Find the slope.
# * Find the intercept.
# * Predict y when x = 10.
X = [[1], [2], [3], [4]]

y = [5, 8, 11, 14]

# Solution
slope = 3
print(slope)
inercept = 5 - (3 * 1)
print(inercept)
