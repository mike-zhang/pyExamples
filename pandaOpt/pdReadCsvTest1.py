#! /usr/bin/env python3 
#-*- coding:utf-8 -*- 

import pandas
import datetime

fpath = r"D:\tmp\1.csv"
#d = pandas.read_table("1.csv",sep=",")
d = pandas.read_csv(fpath,engine='python',encoding="gb2312",converters={'主叫号码':str,'被叫号码':str})
print(d)
print(d.columns)

for index, row in d.iterrows():
    print(row['主叫号码'],row['开始时间'])

dResult = {}
for i in range(24):
    dResult[i] = 0
    
for item in d['开始时间']:
    t1 = datetime.datetime.strptime(item,"%Y-%m-%d %H:%M:%S")
    dResult[t1.hour] += 1
    
for i,v in dResult.items():
    print("%d,%d" % (i,v))
    
#print(d[:1])

