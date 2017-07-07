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
        print self.rcvType
        print self.receivers
     
    def _getObjBase(self,path):
        retobj = None
        if self.docTree :
            retobj = self.docTree.find(path)
        return retobj   
        
    def getSectiontText(self,path):
        retText = ""
        objTmp = self._getObjBase(path)
        if objTmp != None :
            retText = objTmp.text or ""
        return retText.strip()
      
    def getTextAttribute(self,path,attrName):
        retText = ""        
        objTmp = self._getObjBase(path)
        if objTmp != None : 
            retText = objTmp.get(attrName,"")
        return retText.strip()  
        
    def getReceivers(self,path):        
        if not self.docTree : 
            return None            
        objTmp = self.docTree.findall(path)
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
        
        self.smtpServer = self.getSectiontText("smtpServer")
        self.smtpPort = self.getSectiontInt("smtpPort")
        self.sender = self.getSectiontText("sender").strip()
        self.senderPasswd = self.getSectiontText("senderPasswd")
        self.rcvType = self.getTextAttribute("receivers","type")
        self.getReceivers("receivers/user")
        return None

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')      
    
    cnf = ConfigData(defaultFile)
    cnf.show()
    raw_input("test")
        