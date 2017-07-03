#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import sys
import time
import string
import MySQLdb

g_host = '127.0.0.1'
g_port = 3306
g_user = 'root'
g_pswd = ''
g_dbName = 'test'
fpathOut = "out.sql"

def getTableNames(cur):
    sql2exe = "show tables"    
    count = cur.execute(sql2exe)
    if not count : return
    descList = cur.fetchmany(count)
    #print descList
    colNameList = []
    for item in descList :
        colNameList.append(item[0])
    return colNameList

def getTableCreateSql(cur, tbName):
    retStr = ""
    sql2exe = "show create table %s;" % tbName
    count = cur.execute(sql2exe)
    if not count : return
    descList = cur.fetchmany(count)
    if len(descList) > 0:
        retStr = str(descList[0][1])
        print retStr
    retStr += ";\n\n"
    return retStr

def main(host,user,passwd,dbName,port):    
    try:        
        conn=MySQLdb.connect(host,user,passwd,dbName,port)
        cur=conn.cursor()
        fout = open(fpathOut, "w")
        for tbName in getTableNames(cur) :
            ret = getTableCreateSql(cur, tbName)
            fout.write(ret)
        cur.close()
        conn.close()
        fout.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])        

if __name__ == '__main__':
    main(g_host,g_user,g_pswd,g_dbName,g_port)	

    
