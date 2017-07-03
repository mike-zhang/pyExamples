#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

# a simple tcp client
import socket  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('127.0.0.1', 12345))  
sock.send('Test\n')  
print "recv: ",sock.recv(1024)
sock.close()

