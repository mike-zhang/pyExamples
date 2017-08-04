#! /usr/bin/env python
#-*- coding:utf-8 -*-

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01
training_epochs = 40
rng = np.random.RandomState(1)

def fun(x):
    a0,a1,a2,a3,e = 0.1,-0.02,0.03,-0.04,0.05
    y = a0 + a1 * x + a2 * (x**2) + a3 * (x**3)+ e
    y += 0.03 * rng.rand(1)
    return y


trX = np.linspace(-1, 1, 30)
arrY = [fun(x) for x in trX]
num_coeffs = 4
trY = np.array(arrY).reshape(-1,1)

X = tf.placeholder("float")
Y = tf.placeholder("float")

def model(X, w):
    terms = []
    for i in range(num_coeffs):
        term = tf.multiply(w[i], tf.pow(X, i))
        terms.append(term)
    return tf.add_n(terms)

w = tf.Variable([0.] * num_coeffs, name="parameters")
y_model = model(X, w)

cost = tf.reduce_sum(tf.square(Y-y_model))
train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess :
    init = tf.global_variables_initializer()
    sess.run(init)

    for epoch in range(training_epochs):
        for (x, y) in zip(trX, trY):
            sess.run(train_op, feed_dict={X: x, Y: y})

    w_val = sess.run(w)
    print(w_val)

plt.figure() 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid(True)    
plt.title('polynomial regression(tensorflow)') 
plt.scatter(trX, trY)
trX2 = np.linspace(-1, 2, 100)
trY2 = 0
for i in range(num_coeffs):
    trY2 += w_val[i] * np.power(trX2, i)
plt.plot(trX2, trY2, 'r-')
plt.show()
