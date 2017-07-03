#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

from collections import *

data = [('a',1),('b',2),('c',3)]
d1 = dict(data)
d2 = OrderedDict(data)

print d1
print d1.keys()
print d2
print d2.keys()

