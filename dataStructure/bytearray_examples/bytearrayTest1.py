#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

b1 = bytearray(b'123')
b1.append(0x2a)
print b1

b2 = bytearray(b'\x31\x32\x33\x2a')
print b2

for item in b2 :
    print hex(item), 
