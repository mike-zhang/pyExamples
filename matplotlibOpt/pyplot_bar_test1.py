#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13
	
import matplotlib.pyplot as plt  
import datetime
import random

from collections import *

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
  
arrLable = []
arrData = []
for i in range(4):
     arrData.append(random.randint(300,3000))

titleName = u'耗材去向分析'
arrLen = len(arrData)
x = range(arrLen)
for i in range(1,arrLen+1) :
    arrLable.append(u"%d号线" % i )
                          
plt.title(titleName)    

plt.bar(x,arrData,width=0.2)
plt.xticks(x, arrLable)    
plt.grid(False)    

plt.show()  

