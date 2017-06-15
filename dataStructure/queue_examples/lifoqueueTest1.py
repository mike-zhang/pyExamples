#! /usr/bin/env pyton
#-*- coding:utf-8 -*-

from Queue import LifoQueue

q = LifoQueue()
print "put :",
for i in range(5):
    print i,
    q.put(i)

print "\nget :",
while not q.empty():
    print q.get(),


