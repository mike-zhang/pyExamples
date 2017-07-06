#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import pandas
#d = pandas.read_table("1.csv",sep=",")
d = pandas.read_csv("1.csv")
print d
print d.columns
print d[:1]

