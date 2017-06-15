#! /usr/bin/env python
#-*- coding:utf-8 -*-

d1 = {
    "test1" : 10,
    "test2" : 20,
    "test3" : 5,
    "test4" : 2,
    "test5" : 3,
}

print "by key : "
print "min :",min(d1)
print "max :",max(d1)

print "by value : "
print "min :",min(zip(d1.values(),d1.keys()))
print "max :",max(zip(d1.values(),d1.keys()))

