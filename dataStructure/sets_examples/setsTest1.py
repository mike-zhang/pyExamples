#! /usr/bin/env python
#-*- coding:utf-8 -*-

s1 = set([1,2,3])
s2 = set([2,3,4,5,5])
print "s1 :",s1
print "s2 :",s2
print "s1 - s2 :" , s1 - s2 ," or ",s1.difference(s2) # 差集
print "s1 & s2 :" , s1 & s2 ," or ",s1.intersection(s2) # 交集
print "s1 | s2 :" , s1 | s2 ," or ",s1.union(s2) # 并集

