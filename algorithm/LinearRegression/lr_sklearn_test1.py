#! /usr/bin/env python
# -*- coding:utf-8 -*-
# version : Python 2.7.5

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(1)

X = 10 * rng.rand(30)
Y = 1 + 2 * X  + rng.randn(30)
print X
print Y

model = LinearRegression(fit_intercept=True)
model.fit(X[:, np.newaxis], Y)

xfit = np.linspace(0, 20, 100)
yfit = model.predict(xfit[:, np.newaxis])

plt.scatter(X, Y)
plt.plot(xfit, yfit)
plt.show()
