#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import os,sys

defaultFile = "./default.xml"

class ConfigData():        
    def __init__(self,_fileName):
        self.fileName = _fileName
        self.docTree = None
        self.smtpServer = ""
        self.smtpPort = ""
        self.sender = ""
        self.senderPasswd = ""
        self.receivers = []
        self.getConfigFromFile()
        
    def show(self):
        print self.smtpServer
        print self.smtpPort
        print self.sender
        print self.senderPasswd
        print self.receivers
 
    def getSectiontText(self,path):
        retText = ""
        if self.docTree :
            objTmp = self.docTree.find(path)
            if objTmp != None : 
                retText = objTmp.text or ""                
        return retText

    def getReceivers(self):        
        if not self.docTree : 
            return None            
        objTmp = self.docTree.findall("receivers/user")            
        if objTmp :
            self.receivers += [item.text for item in objTmp]            
        return None
        
    def getSectiontInt(self,path):    
        strTmp = self.getSectiontText(path).strip()
        return (int(strTmp) if strTmp.isdigit() else 0)    
    
    def getConfigFromFile(self):        
        try:
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET    
        if not os.path.exists(self.fileName) : 
            print "file ", self.fileName, " not exists"
            return None        
        try:
            self.docTree = ET.ElementTree(file=self.fileName)            
        except Exception,e:
            print "%s is NOT well-formed : %s "%(self.fileName,e)
            return None
        
        self.smtpServer = self.getSectiontText("smtpServer").strip()
        self.smtpPort = self.getSectiontInt("smtpPort")
        self.sender = self.getSectiontText("sender").strip()
        self.senderPasswd = self.getSectiontText("senderPasswd").strip()        
        self.getReceivers()
        return None

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')      
    
    cnf = ConfigData(defaultFile)
    cnf.show()
    raw_input("test")
        