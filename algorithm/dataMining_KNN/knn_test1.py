#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

import math

class KNN:    
    def __init__(self,trainData,trainLabel,k):
        self.trainData = trainData
        self.trainLabel = trainLabel
        self.k = k       
    
    def predict(self,inputPoint):
        retLable = "None"
        arr=[]
        for vector,lable in zip(self.trainData,self.trainLabel):
            s = 0
            for i,n in enumerate(vector) :
                s += (n-inputPoint[i]) ** 2
            arr.append([math.sqrt(s),lable])
        arr = sorted(arr,key=lambda x:x[0])[:self.k]           
        dtmp = {}
        for k,v in arr :
            if not v in dtmp : dtmp[v]=0
            dtmp[v] += 1
        retLable,_ = sorted(dtmp.items(),key=lambda x:x[1],reverse=True)[0]        
        return retLable

data = [
    [1.0, 1.1],
    [1.0, 1.0],
    [0.0, 0.0],
    [0.0, 0.1],
    [1.3, 1.1],
]

labels = ['A','A','B','B','A'] 
knn = KNN(data,labels,3)

print knn.predict([1.2, 1.1])  
print knn.predict([0.2, 0.1])  

