#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

d1 = dict() # or d1 = {}
d1['a'] = 1
d1['b'] = 2
print d1

d1['a'] = 3 # update data
print d1

for k,v in d1.items():
    print k,v

for k,v in d1.iteritems():
    print k,v

print dict.fromkeys(['a','b','c'],True)
print dict.fromkeys("abc",True)



