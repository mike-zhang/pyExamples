#! /usr/bin/env python
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

plt.figure() 
plt.title('polynomial regression') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid(True) 

arrData = [15, 33, 30, 29, 34, 33, 40, 38, 31, 29, 28]
print arrData
N = len(arrData)+1
arrX = range(1,N)
arrY = arrData

X = np.array(arrX).reshape(-1,1)
y = np.array(arrY).reshape(-1,1)

plt.plot(X, y, 'k.')

qf = PolynomialFeatures(degree=6) 
qModel = LinearRegression() 
qModel.fit(qf.fit_transform(X), y) 

#X_predict = np.linspace(100, 200, 100) 
X_predict = np.array(range(1,N+2)).reshape(-1,1)
X_predict_result = qModel.predict(qf.transform(X_predict.reshape(X_predict.shape[0], 1)))
print X_predict_result[-2:]
plt.plot(X_predict,X_predict_result , 'r-') 

plt.show() 