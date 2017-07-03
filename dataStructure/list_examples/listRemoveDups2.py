#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

def rmDups(items):
    tmpSet = set()
    for item in items :
        if not item in tmpSet :
            yield item
            tmpSet.add(item)
            
t1 = [1, 1000, 8, 9, 11, 50, 99, 1, 45, 32, 7, 8, 10]
print t1
print list(rmDups(t1))
