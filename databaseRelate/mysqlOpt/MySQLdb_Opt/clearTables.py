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

sqlList = [
    " delete from tb1; ", 
    " delete from tb2; ", 
    " delete from tb3; ", 
    " delete from tb4; ", 
]


def main(host,user,passwd,dbName,port):    
    try:        
        conn=MySQLdb.connect(host,user,passwd,dbName,port)
        cur=conn.cursor()     
        
        for sql2exe in sqlList:
            print sql2exe
            cur.execute(sql2exe)                    
        conn.commit()          
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])        

if __name__ == '__main__':
    main(g_host,g_user,g_pswd,g_dbName,g_port)	    
    
