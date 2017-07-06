#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

def dict_to_xml(tag,d):
    elem = Element(tag)
    for key,val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

d1 = {'id':1,'name':'test1'}
e=dict_to_xml('student',d1)

print tostring(e)


