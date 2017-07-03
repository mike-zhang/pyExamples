#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import os,sys,re
import MySQLdb

patternInsertSqlStr = re.compile("^INSERT INTO .* VALUES (.*);$")
strValue = "VALUES ("

def IsInsertSqlString(sqlStr):
    retValue = False
    if patternInsertSqlStr.match(sqlStr) : retValue = True
    return retValue  

def doInsert(conn,cur,fileName):
    fin = open(fileName)

    for i,line in enumerate(fin):
        if IsInsertSqlString(line):
            #print line
            num1 = line.find(strValue)
            num1 += len(strValue)        
            sql2exe = "".join([line[:num1], "null",line[line.find(","):]])
            #print sql2exe
            #raw_input()
            #print i            
            cur.execute(sql2exe)
        if (i+1)%10000 == 0 : 
            print i
            conn.commit()
    conn.commit()
    fin.close()
        
if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs != 2:
        print "usage : " + sys.argv[0] + " dirName "
        sys.exit(1)        
    dirName = sys.argv[1]
    if not os.path.isdir(dirName):
        print dirName,"not dir"
        sys.exit(1) 

    sqlFileList = []
    for parent,dirs,files in os.walk(dirName):                
        for fileName in files:
            curPath = os.path.join(parent,fileName)            
            if curPath.split(".")[-1] == 'sql' :
                print curPath  
                sqlFileList.append(curPath)
    try:                
        conn=MySQLdb.connect("127.0.0.1","root","", "test", 3306)
        cur=conn.cursor() 
         
        for filePath in sqlFileList: doInsert(conn, cur,filePath)              

        cur.close()
        conn.close()  
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])  
    
