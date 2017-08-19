#! /usr/bin/evn python
#-*- coding:utf-8 -*-
# python : 2.7.5

import multiprocessing
import threading,time
from Queue import Queue
from taskCommon import worker

gPool = None 
gCount = 99
q = Queue(gCount)

def wokerThread(start,stop):
    #r = gPool.apply(worker,(range(start,stop),))
    r = gPool.apply(worker,(range(1,1000),))
    q.put(r)

def main():
    s = 0
    thrdArr = []
    tStart,tStop = 1,1000
    for i in range(1,gCount+1):
        thrd = threading.Thread(target=wokerThread,args=(tStart,tStop))
        thrdArr.append(thrd)
        tStart = tStop
        tStop += 1000
    for t in thrdArr :
        t.daemon = True
        t.start()    
    while not q.full(): time.sleep(0.1)    
    while not q.empty(): s += q.get()
    print("len : ",len(str(s)))
    print(s%10000)

if __name__ == "__main__":
    gPool = multiprocessing.Pool(4)
    main()


