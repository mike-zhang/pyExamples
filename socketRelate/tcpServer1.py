#! /usr/bin/env python3
#-*- coding:utf-8 -*-
# version : Python 3.11.2

# a simple tcp server
import socket,traceback

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('127.0.0.1', 12345))  
sock.listen(5)  
while True:  
    try :
        connection,address = sock.accept()  
        buf = connection.recv(1024)  
        print(buf)
        connection.send(buf)    
        connection.close()
    except :
        traceback.print_exc()
    
