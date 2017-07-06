#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

from xml.etree.ElementTree import parse,Element

doc=parse('test1.xml')
root=doc.getroot()

#remove element
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# insert new element 
idx = root.getchildren().index(root.find('nm'))
e=Element('spam')
e.text='this is test'  #assign (or update)
root.insert(idx+1,e)

doc.write('new.xml',xml_declaration=True)
