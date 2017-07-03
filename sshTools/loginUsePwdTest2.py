#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

import pexpect 
from getpass import getpass

#passwd = getpass()
passwd = "123456"

def ssh_cmd(user,ip, cmd): 
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user,ip,cmd)) 
    try: 
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'],timeout=5) 
        if i == 0 : 
            ssh.sendline(passwd) 
        elif i == 1: 
            ssh.sendline('yes') 
            ssh.expect('password: ') 
            ssh.sendline(passwd) 
    except pexpect.EOF: 
        print "EOF" 
    except pexpect.TIMEOUT:
        print "TIMEOUT"
    else:
        r = ssh.read() 
        print r
    ssh.close()

if __name__ == '__main__':
    ssh_cmd("root","192.168.1.100","ifconfig")

   
