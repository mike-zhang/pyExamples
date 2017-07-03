#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import MySQLdb
import sys,time
import traceback
import warnings

class ObjDBConnect():
    def __init__(self,host="127.0.0.1",user="root",
                 passwd="",dbname="mysql",port=3306):
        self.conn = None
        self.cursor = None
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port
        warnings.filterwarnings('ignore',category=MySQLdb.Warning)

    def updateConfigure(self,configData):
        self.host = configData.mysqlHost
        self.user = configData.mysqlUser
        self.passwd = configData.mysqlPasswd
        self.dbname = configData.mysqlDbname
        self.port = configData.mysqlPort

    def connect(self,tryTimes=1):
        i = 0
        while i < tryTimes :
            try :
                self.conn = MySQLdb.connect(self.host,self.user,self.passwd,self.dbname,self.port,charset="utf8")
                break
            except Exception:
                i += 1
        return self.conn

    def execute(self,query,doCommit=False):
        '''exec query insert or delete'''
        retCount = 0
        #self.logger.debug(query)
        try:
            cursor = self.conn.cursor()
            retCount = cursor.execute(query)
        except Exception:
            #self.logger.debug("query : {0}".format(query))
            self.connect()
            if self.conn :
                cursor = self.conn.cursor()
                retCount = cursor.execute(query)
        if doCommit :
            #self.logger.debug("before commit")
            self.commit()
            #self.logger.debug("after commit")
        return retCount

    def commit(self):
        if self.conn :
            try :
                self.conn.commit()
            except Exception:
                pass
        return None

    def rollback(self):
        if self.conn :
            try :
                self.conn.rollback()
            except Exception:
                pass
        return None

    def execWithRet(self,query):
        '''exec query '''
        retList = []

        try :
            cursor = self.conn.cursor()
            count = cursor.execute(query)
            retList = cursor.fetchmany(count)
        except Exception:
            #self.logger.debug("query : {0}".format(query))
            self.connect()
            if self.conn :
                cursor = self.conn.cursor()
                count = cursor.execute(query)
                retList = cursor.fetchmany(count)
        return retList

    def close(self):
        if(self.cursor):
            self.cursor.close()
        if self.conn:
            self.conn.commit()
            self.conn.close()

def dbConnectRetry(dbConn,maxRetry):    
    bRet,retryTimes = True,0    
    while True :
        retryTimes += 1    
        if dbConn.connect() : 
            bRet = True
            break
        if retryTimes > maxRetry :                         
            print("connect database error" )
            bRet = False
            break
        print("connect to database,retryTimes : %d"%retryTimes) 
        time.sleep(2)
    return bRet  

def testQuery(host,user,passwd,db,port,charset):
    try:        
        dbConn = ObjDBConnect(host,user,passwd,db,port)        
        if not dbConnectRetry(dbConn,5) : return None        
        result = dbConn.execWithRet("SELECT Host,User FROM user;")
        if len(result) > 0 :
            print result        
        dbConn.close()
    except MySQLdb.Error,e:        
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    except Exception,e :
        print "Error occur : %s" % traceback.format_exc()
    return None
    
if __name__ == "__main__" :
    reload(sys)
    sys.setdefaultencoding('utf-8')       
    print "run as main"
    dbInf = {
        'host' : '127.0.0.1',
        'user' : 'root',
        'passwd' : '',
        'db' : 'mysql',
        'port' : 3306,
        'charset' : "utf8",
    }  
    print testQuery(**dbInf)
else :
    print "import as module"
    

