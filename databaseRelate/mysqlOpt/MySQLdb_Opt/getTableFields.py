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

def getColumName(cur, strTableName):
    #sql2exe = "desc cti_cdr_call"
    sql2exe = "desc " + strTableName
    count = cur.execute(sql2exe)
    if not count : return
    descList = cur.fetchmany(count)
    #print descList
    colNameList = []
    for item in descList : colNameList.append(item[0])                    
    str2Ret = "\"%s\"" %("\",\"".join(colNameList))
    print str2Ret


def main(host,user,passwd,dbName,port):    
    try:        
        conn=MySQLdb.connect(host,user,passwd,dbName,port)
        cur=conn.cursor()          
        getColumName(cur,raw_input("input table name : "))        
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])        

if __name__ == '__main__':
    main(g_host,g_user,g_pswd,g_dbName,g_port)	
    raw_input()
    
