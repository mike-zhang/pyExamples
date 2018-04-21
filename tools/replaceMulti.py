#! /usr/bin/python
#-*- coding: utf-8 -*-  

import os,sys

def doReplace(fpath,src,dst):
    newConent,bFlag = "",False
    with open(fpath,"rb") as fin:
        for line in fin :
            #if len(line.strip()) == 0 : continue
            if line.find(src) == -1 :
                newLine = line
            else:
                bFlag = True
                newLine = line.replace(src,dst)
            newConent += newLine
    if not bFlag : return None
    print fpath
    with open(fpath,"wb") as fout:
        fout.write(newConent)
    return None

def replaceMain(dirName,src,dst):
    for root, dirs, files in os.walk(dirName):
        for name in files:
            fpath = os.path.join(root, name)
            doReplace(fpath,src,dst)
    return None

if __name__ == "__main__":
    if len(sys.argv) < 3 :
        print "usage : replaceMulti srcStr dstStr"
        print "replace current dir files"
        sys.exit(1)
    srcStr = sys.argv[1]
    dstStr = sys.argv[2]
    dirName = "."
    dirName = os.path.realpath(dirName)
    print "working dir :",dirName
    replaceMain(dirName,srcStr,dstStr)
    
    
