#! /usr/bin/env python
#-*- coding:utf-8 -*-

d1 = {"a" : 1, "b" : 2}
d2 = {"c" : 1, "d" : 3}
print "d1:",d1
print "d2:",d2
d1.update(d2)
print "result :",d1

d11 = {"a" : 1, "b" : 2}
d22 = {"c" : 1, "b" : 3}
print "d11:",d11
print "d22:",d22
d11.update(d22)
print "result :",d11


