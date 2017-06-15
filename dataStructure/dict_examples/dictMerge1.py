#! /usr/bin/env python
#-*- coding:utf-8 -*-

d1 = { "a" : 1, "b" : 2 }
d2 = { "c" : 1, "d" : 3 }
d3 = dict(d1,**d2)
print d1
print d2
print d3

d11 = {"a" : 1, "b" : 2}
d22 = {"c" : 1, "b" : 3}
d33 = dict(d11,**d22) # overwrite 
print d11
print d22
print d33


