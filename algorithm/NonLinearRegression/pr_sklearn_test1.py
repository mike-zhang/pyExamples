#! /usr/bin/env python
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def fun(x):
    a0,a1,a2,e = 10,2,-0.03,0.5
    y = a0 + a1 * x + a2 * (x**2) + e
    return y

plt.figure() 
plt.title('quadratic polynomial regression') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid(True) 

arrX = range(-100,100)
arrY = [fun(x) for x in arrX]

X = np.array(arrX).reshape(-1,1)
y = np.array(arrY).reshape(-1,1)
plt.plot(X, y, 'k.')

qf = PolynomialFeatures(degree=2) 
qModel = LinearRegression() 
qModel.fit(qf.fit_transform(X), y) 

X_predict = np.linspace(100, 200, 100) 
X_predict_result = qModel.predict(qf.transform(X_predict.reshape(X_predict.shape[0], 1)))
plt.plot(X_predict,X_predict_result , 'r-') 

plt.show() 