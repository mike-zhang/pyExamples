#! /usr/bin/evn python
#-*- coding:utf-8 -*-
# python : 2.7.5

from multiprocessing import Pool
from taskCommon import worker

def main():
    s = 0
    tStart,tStop = 1,1000
    for i in range(1,100):
        #t = worker(range(tStart,tStop))
        t = worker(range(1,1000))
        s += t
        tStart = tStop
        tStop += 1000
    print("len : ",len(str(s)))
    print(s%10000)

main()


