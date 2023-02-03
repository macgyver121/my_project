# Regression
## 1.Linear Regression (simple)

**Objective**: Find the best target function 

h(x) = θ<sub>0</sub> + θ<sub>1</sub>x

**Cost function**: SSE

**Learning objective**: minimize cost function

**Iterative method**: (Batch) Gradient descent

use learning rate and partial derivative of cost function

If &alpha; is too small, GD can be slow

If &alpha; is too large, GD can overreach the minimum or fail to converge

```
import numpy as np
from sklearn.linear_model import LinearRegression 
x = np.array([[0,2,3]]).T
y = np.array([1,1,4])

lin_reg = LinearRegression()
lin_reg.fit(x, y)
print(lin_reg.intercept_, " , ", lin_reg.coef_)
x_n = np.array([[7, 10]]).T
y_p = lin_reg.predict(x_n)
print(y_p)
```
## 2.Linear Regression (multiple)

**Objective**: Find the best target function 

h(x) = θ<sub>0</sub> + θ<sub>1</sub>x + ... + θ<sub>n</sub>x<sub>n</sub>

**Cost function**: SSE

**Features Scaling**: The goal is to be on s similar scale. This improves the performance and training stability of the model
- Standardization (Z-score)
- Normalization (min-max scale)

**Learning objective**: minimize cost function

**Iterative method**: Gradient descent
- Stochastic
- Mini-batch
- Batch

```
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np
import pandas as pd
# import os
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

data = pd.read_csv('https://raw.githubusercontent.com/ekaratnida/Applied-machine-learning/master/Week04-workshop-1/data.txt')

data['bathroom'] = np.random.randint(1,5,size = 47)

print(data.head())

x = data[['area', 'rooms', 'bathroom']]
print(x.head())

y = data[["price"]] 
print(y.head())

"""Train model"""
print("Train")
lin_reg = LinearRegression()
lin_reg.fit(x, y)
print(lin_reg.intercept_)
print(lin_reg.coef_)

"""Predict"""
print("Predict")
#X_test = np.array([[2000,6]])
x_test = pd.DataFrame(
    {
    "area":[2000,3000],
    "rooms":[6,3],
    "bathroom": [2,3]
    }
)

result = lin_reg.predict(x_test)
print(result)
```
![image](https://user-images.githubusercontent.com/85028821/216637476-530f3ad3-d8bc-4232-ab8c-a045614e434e.png)

## 3.Polynomial Regression

h(x) = θ<sub>0</sub> + θ<sub>1</sub>x + θ<sub>2</sub>x<sup>2</sup>

Change to Polynomial Features and use Linear Regression method
```
# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X_train)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y_train)

# Visualizing the Polymonial Regression results
#print(np.sort(X_train,axis=None))
test = pol_reg.predict(poly_reg.fit_transform(X_train))
#print(np.sort(test,axis=None))
plt.scatter(X_train, y_train, color='red')
plt.scatter(X_test, y_test, color='yellow')
plt.plot(np.sort(X_train,axis=None), np.sort(test,axis=None), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
```
![image](https://user-images.githubusercontent.com/85028821/216638017-16fe03be-be95-4e6b-b1f7-50aa60ee0874.png)

# Classification
## 1.Logistic Regression
