#! /usr/bin/python
#-*- coding:utf-8 -*-

# a simple udp server

import socket, traceback

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1",12345))

while True:
    try:
        message, address = s.recvfrom(1024)
        print "Got data from", address
        print message
        s.sendto(message, address)
    except :
        traceback.print_exc()
        