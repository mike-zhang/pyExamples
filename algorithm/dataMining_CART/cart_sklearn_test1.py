#! /usr/bin/env python
#-*- coding:utf-8 -*-

from sklearn import tree
import numpy as np

# scikit-learn使用的决策树算法是CART

X = [[0,0],[1,1]]
Y = ["A","B"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

data1 = np.array([2.,2.]).reshape(1,-1)
print clf.predict(data1) # 预测类别  
print clf.predict_proba(data1) # 预测属于各个类的概率

