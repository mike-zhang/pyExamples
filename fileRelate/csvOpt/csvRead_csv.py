#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import csv
with open("1.csv") as fin:
    for line in csv.reader(fin):
        print line
