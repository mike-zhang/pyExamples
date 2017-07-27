#! /usr/bin/python
#-*- coding: utf-8 -*-
# version : Python 2.7.13

class Base():
    id = 0
    name = ""
    
    def doShow(self):
        pass
    
    def show(self):        
        assert(self.name)
        self.doShow()        
        
class A(Base):
    def __init__(self,id,name):
        self.id = id
        self.name = name       
    def doShow(self):
        print self.id,self.name

if __name__ == '__main__':        
    a = A(1,'test')
    a.show()    
else :
    print "import module"