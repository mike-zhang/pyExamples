#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.5

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(1)
N = 10

X = np.array(N * [10 * rng.rand(2)])
b = [2, 3]
Y = 1 + np.matmul(X,b)  + rng.randn(N)

print X
print Y

model = LinearRegression()
model.fit(X, Y)

xfit = np.array(10 * [10 * rng.rand(2)])
yfit = model.predict(xfit)

print "xfit :"
print xfit
print "yfit :"
print yfit


    

