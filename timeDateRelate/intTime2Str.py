#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import time,datetime,re,dateutil
import pandas as pd

def intTime2Str(unixTimeInt):
    if unixTimeInt < 0 : unixTimeInt = 0
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(unixTimeInt))    

def intTime2Str_2(unixTimeInt):    
    if unixTimeInt < 0 : unixTimeInt = 0
    return datetime.datetime.fromtimestamp(unixTimeInt).strftime("%Y-%m-%d %H:%M:%S")
    
def intTime2Str_3(unixTimeInt):        
    if unixTimeInt < 0 : unixTimeInt = 0
    return pd.datetime.fromtimestamp(unixTimeInt).strftime("%Y-%m-%d %H:%M:%S")    
  
t1 = time.time()
print t1   
print "intTime2Str : ",intTime2Str(t1)
print "intTime2Str_2 : ",intTime2Str_2(t1)
print "intTime2Str_3 : ",intTime2Str_3(t1)

