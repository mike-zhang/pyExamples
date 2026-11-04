#! /usr/bin/python3 
#-*- coding:utf-8 -*-

import os

def doGitPush():
    bNameAll = os.popen("git branch -l").read()
    #print bNameAll
    bName = ""
    for item in bNameAll.split('\n'):            
        if item[0] == '*' :
            bName = item
            break
    #print bName
    bName = bName.split()[-1]
    print(bName)
    # 如果不存在则创建远程分支     
    strCmd = "git push origin %s:%s" % (bName,bName) 
    # 删除远程分支： "git push origin :%s" % bName
    print(strCmd)
    os.system(strCmd)
    os.system("git push origin --tags") # 同步标签
    

doGitPush()
