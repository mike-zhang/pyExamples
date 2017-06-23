#! /usr/bin/env python
#-*- coding:utf-8 -*-

import ftplib 

ftp = ftplib.FTP('127.0.0.1')   
#ftp.login("UID", "PSW")
ftp.login()  # user anonymous, passwd anonymous@
ftp.retrlines('LIST')

