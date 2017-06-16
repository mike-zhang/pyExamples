#! /usr/bin/env python 
#-*- coding:utf-8 -*-

import warnings 

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import paramiko 
 
hostname='192.168.1.100' 
username='root' 
keyFilePath = "./rsaPri" # openssh private key file
port=22 
if __name__=='__main__':  
    key=paramiko.RSAKey.from_private_key_file(keyFilePath) 
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname,port,username,pkey=key)
    stdin,stdout,stderr=s.exec_command('ifconfig')
    print stdout.read()
    s.close()
    