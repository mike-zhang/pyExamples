#! /usr/bin/env python
#-*- coding:utf-8 -*-

'''
调用对象上的方法，方法以字符串形式给出
'''
import math
import operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)
    
    def distance(self, x, y):
        return math.hypot(self.x - x, self.y -y)
    
p = Point(2, 3)
d = getattr(p, "distance")(0, 0)
print(d)

d2 = operator.methodcaller('distance', 0, 0)(p)
print(d2)

