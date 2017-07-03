#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

fName = "1.txt"
with open(fName,"r") as fin :
    for line in fin :
        print line
        
