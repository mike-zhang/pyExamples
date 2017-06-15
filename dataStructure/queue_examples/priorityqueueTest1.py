#! /usr/bin/env python
#-*- coding:utf-8 -*-

from Queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0
    def put(self,item,priority):
        PriorityQueue.put(self,(priority,self.counter,item))
        self.counter += 1

    def get(self,*args,**kwargs):
        _,_,item = PriorityQueue.get(self,*args,**kwargs)
        return item

q = MyPriorityQueue()
q.put("item1",2)
q.put("item2",1)

while not q.empty():
    print q.get()



