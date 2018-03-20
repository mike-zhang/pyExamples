#! /usr/bin/env python
# -*- coding:utf-8 -*-

import struct

def htonfl(f):
    s = struct.pack('d',f)
    return struct.unpack('!Q',s)[0]

def fltonl(v):
    s = struct.pack('!Q',v)
    return struct.unpack('d',s)[0]

a = 123.456
print a
b = htonfl(a)
print b , hex(b)
print fltonl(b)


