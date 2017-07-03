#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

# a simple udp client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dstHost = ('127.0.0.1', 12345)
client.sendto('3',dstHost)
print "recv : ",client.recv(1024)

