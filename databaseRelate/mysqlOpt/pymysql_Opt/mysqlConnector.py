#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import pymysql
import logging,traceback,time,sys

logging.basicConfig(
    level=logging.DEBUG, # DEBUG,INFO,WARNING,ERROR,CRITICAL
    format='%(asctime)s %(filename)s[line:%(lineno)d] [%(levelname)s] : %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'
)

class ObjDBConnect():    
    def __init__(self,host="127.0.0.1",user="root",
                 passwd="",db="mysql",port=3306):
        self.conn = None        
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.lastCommitTime = int(time.time())        
        self.logger = logging.getLogger()

    def connect(self,tryTimes=1):
        i = 0
        while i < tryTimes :            
            try :
                self.conn = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    port=self.port,
                    passwd=self.passwd,
                    db=self.db,
                    charset="utf8", 
                )
                self.logger.debug("connect ok!current retry : {0}".format(i))
                break
            except Exception:
                i += 1
                self.logger.error(traceback.format_exc())
        return self.conn
        
    def execute(self,sql,doCommit=False):
        '''exec sql insert update or delete'''        
        retCount = 0
        self.logger.debug(sql)        
        try:            
            cur = self.conn.cursor()            
            retCount = cur.execute(sql)
        except Exception:
            self.connect()
            if self.conn :
                retCount = self.conn.cursor().execute(sql)                
        if doCommit :            
            self.commit()            
        return retCount

    def commit(self):    
        if self.conn :        
            try :                
                curTime = int(time.time())
                if int(curTime - self.lastCommitTime) > 0:
                    self.lastCommitTime = curTime
                    self.conn.commit()
            except Exception:
                self.logger.error(traceback.format_exc())
        return None

    def rollback(self):
        if self.conn :
            try :
                self.conn.rollback()
            except Exception:
                pass
        return None

    def _real_execWithRet(self,sql):
        cursor = self.conn.cursor()
        self.logger.debug(sql)
        count = cursor.execute(sql)        
        self.logger.debug("count = {0}".format(count))        
        for row in cursor:
            yield row
        #return cursor.fetchmany(count)        
    
    def execWithRet(self,sql):
        '''exec sql query '''
        retList = []        
        try :
            retList = list(self._real_execWithRet(sql))            
        except Exception:
            self.connect()
            if self.conn :
                retList = list(self._real_execWithRet(sql))
        return retList

    def close(self):        
        if self.conn:
            self.conn.commit()
            self.conn.close()

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
    }  
    
    query = "SELECT Host,User FROM user"
    dbTest1 = ObjDBConnect(**dbInf)
    dbTest1.connect()            
    print list(dbTest1.execWithRet(query))
    print "_real_execWithRet : "
    ret = dbTest1._real_execWithRet(query)    
    print ret.next()
    print "*" * 10
    for item in ret :
        print item
else :
    print "import as module"            
            

