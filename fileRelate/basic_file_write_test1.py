#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

fName = "1.txt"
with open(fName,"w") as fout :    
    for i in range(10):
        fout.write("msg_%d\r\n" % i)
    
