#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import xml.etree.ElementTree as ET

#import lxml.etree as ET
    
if __name__ == "__main__" :
    filePath = "default.xml"
    try :
        ET.parse(filePath)
        print "xml parse success"
    except Exception,e :
        print "xml parse error"
        print "error info : ",e
    
            