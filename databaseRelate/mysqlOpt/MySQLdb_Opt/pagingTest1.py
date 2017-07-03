#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

from mysqlConnector import ObjDBConnect

tbName="objeventlog"

def exeSqlAndGetInt(dbConn,sql2exe):    
    retVavlue = 0  
    tmpList = dbConn.execWithRet(sql2exe)
    if len(tmpList) == 1 :             
        if str(tmpList[0][0]).isdigit(): retVavlue = int(tmpList[0][0])            
    return retVavlue

def main():
    dbInf = {
        'host' : '127.0.0.1',
        'user' : 'root',
        'passwd' : '',
        'dbname' : 'test',
        'port' : 3306,          
    }     
    dbConn = ObjDBConnect(**dbInf)
    sqlCount = "select count(*) from %s " % tbName    
    totalNum = exeSqlAndGetInt(dbConn,sqlCount)    
    step, i = 10, 0
    sqlBase = "select * from %s " % tbName
    while i <= totalNum :
        sqlTmp = "{} limit {},{}".format(sqlBase, i, step)
        print sqlTmp
        for item in dbConn.execWithRet(sqlTmp):
            #print item
            print item[0]
        i += step        
        
if __name__ == "__main__":
    main()