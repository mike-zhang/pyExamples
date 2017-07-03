#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import MySQLdb
import os,sys,csv,traceback
import logging,tarfile,time

lableId = "id"

logger = logging.getLogger()
    
def initLoggerConsole():
    logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S')    

def entryExit():    
    def _deco(func):
        def __deco(*args, **kwargs):
            logger.info("before %s called" % func.__name__)
            func(*args, **kwargs)
            logger.info("after %s called" % func.__name__)            
        return __deco
    return _deco
 
    
class ObjDBConnect():
    conn = None
    cursor = None
    
    def __init__(self,host,user,passwd,dbname,port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port
        
    def connect(self,tryTimes=1):
        i = 0
        while i < tryTimes :                      
            try :
                self.conn = MySQLdb.connect(self.host,self.user,self.passwd,self.dbname,self.port,charset="utf8")
                break
            except : 
                i += 1                
        return self.conn        
        
    def execute(self,sql):
        '''exec sql insert'''
        ret = 0
        try:
            cursor = self.conn.cursor()
            ret = cursor.execute(sql)
        except (AttributeError,MySQLdb.OperationalError, MySQLdb.DatabaseError):            
            logger.error(traceback.format_exc())
            logger.error("sql:{0}".format(sql))
            self.connect()
            if self.conn:
                cursor = self.conn.cursor()
                ret = cursor.execute(sql)
        return ret
    
    def commit(self):
        if self.conn : self.conn.commit()
        
    def rollback(self):
        if self.conn : self.conn.rollback()
  
    def close(self):
        if(self.cursor):
            self.cursor.close()
        if self.conn:
            self.conn.commit()
            self.conn.close()
@entryExit()
def dbConnectRetry(dbConn,maxRetry):
    bRet,retryTimes = True,0    
    while True :
        retryTimes += 1    
        if dbConn.connect() : 
            bRet = True
            break
        if retryTimes > maxRetry :    
            strLog = "connect database error"            
            logger.error(strLog)
            bRet = False
            break
        logger.warn("connect to database,retryTimes : %d"%retryTimes) 
        time.sleep(2)
    return bRet   
    
@entryExit()
def unTargzFiles(dirName):
    for root, dirs, files in os.walk(dirName):
        for fName in files:
            tmpPath = os.path.join(root, fName)            
            if fName.split(".")[-1] != "gz" : continue
            try : 
                tar = tarfile.open(tmpPath)        
                for name in tar.getnames() : 
                    tar.extract(name,path=root)
                tar.close()        
            except Exception, e:                
                logger.error(traceback.format_exc())
    return None    
    
class TableDataRestore():
    def __init__(self,csvDir,dbHost,dbPort,dbUser,dbPwd,dbName,tableName):
        self.csvDir = csvDir
        self.dbHost = dbHost
        self.dbPort = dbPort
        self.dbUser = dbUser
        self.dbPwd = dbPwd
        self.dbName = dbName        
        self.tableName = tableName        
        
    @entryExit()
    def restoreDataFromFile(self,fName) :        
        conn = ObjDBConnect(self.dbHost,self.dbUser,self.dbPwd,self.dbName,self.dbPort)    
        dbConnectRetry(conn,5)        
        fin = open(fName,"rb")        
        tableSection = []
        for i,line in enumerate(csv.reader(fin)):
            #print line        
            if i == 0 :
                tableSection = list(line)
                continue        
            dtmp = dict(zip(tableSection,line))
            sqlDelete = "delete from  %s where %s = %d;" % (self.tableName,lableId,int(dtmp.get(lableId,-1)))
            sqlInsert = "insert into %s (" % self.tableName
            sqlInsert += ",".join(tableSection)
            sqlInsert += ") values ('"
            sqlInsert += "','".join(line) + "');"
            #print sqlInsert
            #raw_input()
            try :                
                conn.execute(sqlDelete)
                conn.execute(sqlInsert)
                #print i
                if i % 10000 == 1 : 
                    print i
                    conn.commit()
            except Exception,e:
                print "Exception : %s" % e     
                continue
        conn.commit()
        fin.close() 
        
    @entryExit()
    def restoreTable(self) : 
        for root, dirs, files in os.walk(self.csvDir) :
            for name in files :
                fName = os.path.join(root, name)                
                if name.split(".")[-1] != "csv" : continue                
                self.restoreDataFromFile(fName)

@entryExit()                
def doTableRecovery(params):
    try :              
        tbRestore = TableDataRestore(*params)
        tbRestore.restoreTable()
    except Exception ,e :
        print traceback.format_exc()
        logger.error(traceback.format_exc())

if __name__ == '__main__': 
    reload(sys)
    sys.setdefaultencoding('utf-8')      
    
    numargs = len(sys.argv)
    if numargs != 3:
        print "usage : " + sys.argv[0] + " csvTargzDirName tableName"
        sys.exit(1)        
    print "csvTargzDirName : %s" % sys.argv[1]
    print "tableName : %s" % sys.argv[2]
    csvTarDir = os.path.abspath(sys.argv[1])
    tableName = sys.argv[2]
    
    host,port,user,pwd,dbName = "127.0.0.1",3306,"root","","test"
    
    params = [csvTarDir,host,port,user,pwd,dbName,tableName]
    
    try :
        initLoggerConsole()        
        unTargzFiles(csvTarDir)        
        doTableRecovery(params)       
        
    except Exception ,e :        
        logger.error(traceback.format_exc())
          
    
