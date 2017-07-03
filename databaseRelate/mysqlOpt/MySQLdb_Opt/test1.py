#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import MySQLdb

dbConn = MySQLdb.connect('127.0.0.1','root','','mysql',3306,charset="utf8")
query = "SELECT Host,User FROM user"

cursor = dbConn.cursor()
count = cursor.execute(query)
retList = cursor.fetchmany(count)

for item in retList:
    print item
    
dbConn.close()
           
