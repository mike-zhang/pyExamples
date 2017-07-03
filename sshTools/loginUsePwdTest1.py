#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

import warnings 

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import paramiko 
 
hostname='192.168.1.100' 
username='root' 
password='123456' 

#paramiko.util.log_to_file('paramiko.log')
s=paramiko.SSHClient() 
#s.load_system_host_keys() 
s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
s.connect(hostname = hostname,username=username, password=password) 
stdin,stdout,stderr=s.exec_command('ifconfig;free;df -h')     
print stdout.read() 
s.close() 
raw_input()
