#! /usr/bin/env python
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

rng = np.random.RandomState(1)

def fun(x):
    a0,a1,a2,a3,e = 0.1,-0.02,0.03,-0.04,0.05
    y = a0 + a1 * x + a2 * (x**2) + a3 * (x**3)+ e
    y += 0.03 * rng.rand(1)
    return y

plt.figure() 
plt.title('polynomial regression(sklearn)') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid(True) 

X = np.linspace(-1, 1, 30)
arrY = [fun(x) for x in X]
X = X.reshape(-1,1)
y = np.array(arrY).reshape(-1,1)

plt.plot(X, y, 'k.')

qf = PolynomialFeatures(degree=3) 
qModel = LinearRegression() 
qModel.fit(qf.fit_transform(X), y) 

X_predict = np.linspace(-1, 2, 100) 
X_predict_result = qModel.predict(qf.transform(X_predict.reshape(X_predict.shape[0], 1)))
plt.plot(X_predict,X_predict_result , 'r-') 

plt.show() 