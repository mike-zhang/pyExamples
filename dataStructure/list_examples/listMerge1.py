#! /usr/bin/env python
#-*- coding:utf-8 -*-

t1 = [1,2,3]
t2 = [3,4]

print t1 + t2
print t1,t2

print sum([t1,t2],[])
print t1,t2

t1.extend(t2)
print t1,t2

