# Regression
## Linear Regression (simple)

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
## Linear Regression (multiple)

**Objective**: Find the best target function 

h(x) = θ<sub>0</sub> + θ<sub>1</sub>x + ... + θ<sub>n</sub>x<sub>n</sub>
