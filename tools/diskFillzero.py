#!/usr/bin/env python
#-*- coding:utf-8 -*-

with open("1.zero","wb") as fout:
    while 1:
        try :
            fout.write(b'\x00' * 1024 * 1024 )
        except :
            break

