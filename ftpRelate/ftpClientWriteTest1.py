#! /usr/bin/env python
#-*- coding:utf-8 -*-

import ftplib

filename = "1.txt"
ftp = ftplib.FTP("127.0.0.1")
ftp.login() # user anonymous, passwd anonymous@
#ftp.login("UID", "PSW")
ftp.cwd("/pub")

with open(filename, 'r') as fin :
    ftp.storlines('STOR ' + filename, fin)
