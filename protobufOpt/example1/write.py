#! /usr/bin/env python
#-*- coding:utf-8 -*-

import addr.book_pb2 as book_pb2
import google.protobuf
 
msg1 = book_pb2.book()
msg1.id = 1
msg1.str = "testMsg1"
#print msg1

msgBinary = msg1.SerializeToString() 
 
with open("log", "wb") as f: 
    f.write(msgBinary)


