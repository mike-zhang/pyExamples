#! /usr/bin/evn python
#-*- coding:utf-8 -*-
# python : 2.7.5

def worker(arr):
    s = 0
    for n in arr :
        arrTmp = range(1,n+1)
        if len(arrTmp) == 0 : continue
        rtmp = 1
        for i in arrTmp :
            rtmp *= i
        s += rtmp
    return s

