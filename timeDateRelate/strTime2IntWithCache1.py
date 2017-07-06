#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import re,time
from datetime import datetime

class TimeConvert(object):
    def __init__(self):
        self.dCache = {}
        self.patternStrTime = re.compile('(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})')
        self.dTimeTable = {}
        self.initTimeTable()
        
    def intTime2Str(self,unixTimeInt):
        if unixTimeInt < 0 : unixTimeInt = 0
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(unixTimeInt))
    
    def initTimeTable(self):
        for i in xrange(3600):
            seconds = i % 60
            minutes = (i / 60) % 60
            strTmp = "%02d:%02d" % (minutes,seconds)
            #print strTmp
            self.dTimeTable[i] = strTmp
        return None
    
    def strTime2Int(self,strTime):
        ret = self.dCache.get(strTime, 0)       
        if ret == 0:
            if not self.patternStrTime.match(strTime) :
                #print "\"%s\" is not time string format" % strTime
                ret = int(time.time())
            else :
                #self.dCache.clear()
                if len(self.dCache) > 3600 * 2 : self.dCache.clear()                
                tmpList = self.patternStrTime.search(strTime).groups()
                ret = int(time.mktime(datetime(* map(int,tmpList)).timetuple()))
                self.dCache[strTime] = ret                           
                for i in xrange(1, 3600 - ret % 3600):
                    time_int = ret + i                
                    j = time_int % 3600                            
                    #print dTimeTable[j]
                    time_str = strTime[:-5] + self.dTimeTable[j]                
                    self.dCache[time_str] = time_int
        else :
            print "data in cache"
            #pass
        return ret   

tc = TimeConvert()        
sArr = [
    "2016-05-19 14:06:09",
    "2016-05-19 14:07:09",
    "2016-05-19 14:08:09",
]


for item in sArr :
    print tc.strTime2Int(item)
        
raw_input()        

