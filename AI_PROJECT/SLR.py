# import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
print(dir(plt))

# sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1,1) # Independent variables
y = np.array([10000,19000,30000,40000,50000]) # dependent variables

# create a linear regression model
model = LinearRegression()

# fit the model to the data
model.fit(X, y)
y_pred = model.predict(X)

# plot the orginal data and the regression linear
plt.scatter(X, y, label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('Single Linear Regression')
plt.show()

print(dir(np))

# coefficient and intercept
print("Slope (Coefficient):", model.coef_)
print("Intercept:",model.intercept_)

