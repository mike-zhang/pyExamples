#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import xml.etree.ElementTree as ET

#import lxml.etree as ET

confStr = '''
<config>
    <task1>
        <lable1>dddd</lable1>
    </task1>
</config>
'''

if __name__ == "__main__" :
    docTree = ET.fromstring(confStr)    
    if len(docTree) :
        objTmp = docTree.find('task1/lable1')
        if objTmp != None :
            print objTmp.text
        
    