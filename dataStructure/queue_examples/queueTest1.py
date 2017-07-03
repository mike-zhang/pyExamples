#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

from Queue import Queue

q = Queue()
for i in range(5):
    q.put(i)

q.put((1,2,3))
while not q.empty():
    print q.get(),


