#! /usr/bin/env python3
#-*- coding:utf-8 -*-
# version : Python 3.11.2

# a simple tcp client
import socket  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('127.0.0.1', 12345))  
sock.send(b'Test\n')  
print("recv: ",sock.recv(1024))
sock.close()

