#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import ibm_db

dbCnnInfo = {
    'HOSTNAME':'192.168.1.100',
    'DATABASE':'testdb',
    'PORT':'50000',
    'UID':'admin',
    'PWD':'123456',
    'PROTOCOL':'TCPIP',
}

#cnnStr = "DATABASE=%s;HOSTNAME=%s;PORT=%s;PROTOCOL=TCPIP;UID=%s;PWD=%s"%(database,hostname,port,user,password)
cnnStr = ";".join(["%s=%s"%(k,v) for k,v in dbCnnInfo.items()])
conn=ibm_db.connect(cnnStr,"","")
result = ibm_db.exec_immediate(conn,"select * from tb1")
row = ibm_db.fetch_assoc(result)
while row:
    #print row.get('name'),row.get('age')
    print row
    row = ibm_db.fetch_assoc(result)
#ibm_db.exec_immediate(conn,"insert into  student value('chen',29)")
#ibm_db.commit(conn)
ibm_db.close(conn)


