#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import time,datetime,re,dateutil
import pandas as pd

patternStrTime = re.compile('(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})')
def strTime2Int(strTime):            
    #patternStrTime = re.compile('(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})')    
    if not patternStrTime.match(strTime) :     
        #print "\"%s\" is not time string format" % strTime
        return 0        
    return int(time.mktime(datetime.datetime(* map(int,patternStrTime.search(strTime).groups()) ).timetuple()))    

def strTime2Int_2(strTime):            
    ts=pd.to_datetime(strTime)
    return ts.value/(10**9)
   
def strTime2Int_3(strTime):
    ts = time.mktime(dateutil.parser.parse(strTime).timetuple())
    return int(ts)

s1 = '2017-07-05 00:00:00'
print s1   
print "strTime2Int : ",strTime2Int(s1)
print "strTime2Int_2 : ",strTime2Int_2(s1)
print "strTime2Int_3 : ",strTime2Int_3(s1)
