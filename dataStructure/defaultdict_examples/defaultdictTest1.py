#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

from collections import *

d1 = defaultdict(int)
print d1
print d1['a']
d1['b'] += 3
print d1['b']

d2 = defaultdict(list)
d2['a'].append(1)
d2['b'] += [1,2,3]
print d2

