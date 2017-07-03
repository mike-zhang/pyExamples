#! /usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys,time,datetime,MySQLdb,csv

lableId = "id"

def getColumName(cur, strTableName):
    sql2exe = "desc " + strTableName
    count = cur.execute(sql2exe)
    if not count : return
    descList = cur.fetchmany(count)
    #print descList
    colNameList = []
    for item in descList : colNameList.append(item[0])                        
    return tuple(colNameList)

def genSqlSelectHeader(tableFields):
    sqlTmp = "select "
    for field in tableFields:        
        sqlTmp += field
        if field != tableFields[-1]: sqlTmp += ","
    return sqlTmp

def doBackUpToCsv(cur,tableName,maxPerFetch,filePath):        
    tableFields = getColumName(cur,tableName)
    foutCSV = open(filePath, 'wb')
    if not foutCSV :        
        print "doBackUpToCsv : open %s failed!"%filePath        
        return 0     
    print "csvFilePath : %s"%filePath
    csvWriter = csv.writer(foutCSV)    
    csvWriter.writerow(tableFields)   
    start = 0  
    while 1:
        originStart = start        
        sqlTmp = genSqlSelectHeader(tableFields)
        sqlTmp += " from %s where %s >= %d limit %d" % (tableName,lableId,start,maxPerFetch)
        #print sqlTmp
        count = cur.execute(sqlTmp)       
        if count == 0 : break              
        tmpList = cur.fetchmany(maxPerFetch) 
        
        for item in tmpList : 
            dictTmp = dict(zip(tableFields,item))
            start = dictTmp[lableId]                 
            csvWriter.writerow(item) # backup data to csvFile                        
        foutCSV.flush()
        if start < originStart + maxPerFetch :
            start = originStart + maxPerFetch        
    foutCSV.close()
    return 1
    
def main(host,user,passwd,dbname,port,tableName,backupFilePath):
    try:                
        conn=MySQLdb.connect(host,user,passwd,dbname,port,charset="utf8")
        cur=conn.cursor()       
        doBackUpToCsv(cur,tableName,10000,backupFilePath)                    
        cur.close()
        conn.close()  
    except MySQLdb.Error,e:
        strLog = "Mysql Error %d: %s" % (e.args[0], e.args[1])  
        print strLog
        return 

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')      
    numargs = len(sys.argv)
    if numargs != 3:
        print "usage : " + sys.argv[0] + " tableName outputCsvFilePath "
        sys.exit(1)        
    tableName = sys.argv[1]
    csvFilePath = sys.argv[2]    
    main("127.0.0.1","root","","test",3306,tableName,csvFilePath)
    
    
    
