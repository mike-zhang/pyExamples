#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import xml.etree.ElementTree as ET

#import lxml.etree as ET

if __name__ == "__main__" :
    docTree = ET.parse("default.xml")   
    if docTree :
        objTmp = docTree.find('task1/lable1')
        if objTmp != None :
            print objTmp.text
        
    