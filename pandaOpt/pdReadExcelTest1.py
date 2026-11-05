#! /user/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd

xlsx2 = pd.read_excel('test1.xls','Sheet1')

for i in range(len(xlsx2)):
    for tag in xlsx2.columns:
        print(xlsx2[tag][i])

print(xlsx2.to_dict())

dtmp = dict(zip(xlsx2.columns,xlsx2.loc[0].values))
print(dtmp)


# 遍历方法
for index,row in xlsx2.iterrows():
	print(row['主叫'],row['呼叫时间'])
	
xlsx2 = pd.read_excel('111.xls')
print(xlsx2.columns) #输出列名称
print(sum(xlsx2['号码费用'])) #计算某列的和
  
