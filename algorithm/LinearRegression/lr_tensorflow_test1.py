#! /usr/bin/env python
#-*- coding:utf-8 -*-
#python version : 2.7.5
#tensorflow version : 1.2.1

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

N = 200  # 样本数据格式
trainNum = 30 # 训练次数

# 公式 ： y = w * x + b

X = np.linspace(-1, 1, N)
Y = 3.0 * X + np.random.standard_normal(X.shape) * 0.3 + 0.9 
X = X.reshape([N, 1])
Y = Y.reshape([N, 1])

# 期望的图
plt.scatter(X, Y)
plt.plot(X, 3.0 * X + 0.9)
plt.show()

# 建模
inputX = tf.placeholder(dtype=tf.float32, shape=[None, 1])
outputY = tf.placeholder(dtype=tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([1, 1], stddev=0.01))
b = tf.Variable(tf.random_normal([1], stddev=0.01))
pred = tf.matmul(inputX, W)+b
loss = tf.reduce_sum(tf.pow(pred - outputY, 2))

train = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
tf.summary.scalar("loss", loss)
merged = tf.summary.merge_all()
init = tf.global_variables_initializer()

# 训练
with tf.Session() as sess:
    sess.run(init)
    for i in range(trainNum):
        sess.run(train,feed_dict={inputX : X, outputY : Y})
        predArr, lossArr = sess.run([pred, loss], feed_dict={inputX : X, outputY : Y})
        # print "lossArr : ",lossArr
        # print "predArr : ",predArr
        summary_str = sess.run(merged, feed_dict={inputX : X, outputY : Y})
        WArr, bArr = sess.run([W, b])
        print(WArr, bArr)        

# 预测的图
plt.scatter(X, Y)
plt.plot(X , WArr * X + bArr) 
plt.show()


