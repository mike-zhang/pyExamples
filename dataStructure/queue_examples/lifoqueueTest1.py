#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

from Queue import LifoQueue

q = LifoQueue()
print "put :",
for i in range(5):
    print i,
    q.put(i)

print "\nget :",
while not q.empty():
    print q.get(),


