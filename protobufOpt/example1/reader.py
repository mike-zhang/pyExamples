#! /usr/bin/env python
#-*- coding:utf-8 -*-

import addr.book_pb2 as book_pb2
import google.protobuf
 
msg1 = book_pb2.book()
msgBinary = None
with open("log", "rb") as f: 
	msgBinary = f.read()

if msgBinary :
	msg1.ParseFromString(msgBinary)

print msg1
