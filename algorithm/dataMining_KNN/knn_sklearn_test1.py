#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

from sklearn import neighbors  
import numpy

data = [
    numpy.array([1.0, 1.1]),
    numpy.array([1.0, 1.0]),
    numpy.array([0.0, 0.0]),
    numpy.array([0.0, 0.1]),
    numpy.array([1.3, 1.1])
]
labels = ['A','A','B','B','A'] 

knn = neighbors.KNeighborsClassifier(n_neighbors=3)  
knn.fit(data, labels)  

print knn.predict(numpy.array([1.2, 1.1]).reshape(1,-1))  
print knn.predict(numpy.array([0.2, 0.1]).reshape(1,-1))  
