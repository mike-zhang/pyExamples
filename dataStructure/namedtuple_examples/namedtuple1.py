#! /usr/bin/env python
#-*- coding:utf-8 -*-

from collections import namedtuple

Student = namedtuple('Student',['id','name','score'],verbose=False)

s1 = Student(1,'s1',81)
print s1
s1 = s1._replace(id=123)
print s1
a,b,c = s1
print a,b,c
print s1.id,s1.name,s1.score

arrTest = [(1,'test1',90),(2,'test2',95)]
for s in arrTest :
    stu = Student._make(s)
    print stu


