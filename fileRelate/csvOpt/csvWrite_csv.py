#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import csv
with open("mydata.csv","wb") as fout:
    writer = csv.writer(fout)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
    
