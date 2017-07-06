#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import smtplib

smtpServer='smtp.163.com'
smtpPort='25'
sender = 'test1@163.com'
senderPasswd = "****"
receivers = ['test2@qq.com',]

def getMailContent(strContent):
    msg2Snd = "From: <" + sender + ">\n"
    msg2Snd += "To: <" + receivers[0] + ">\n"
    msg2Snd += "Subject: test\n\n"        
    msg2Snd += strContent + "\n"    
    return msg2Snd
            
try:       
    smtpObj = smtplib.SMTP(smtpServer,smtpPort)
    smtpObj.ehlo()
    smtpObj.login(sender,senderPasswd)
    smtpObj.sendmail(sender, receivers, getMailContent("just a test"))
    print "Successfully sent email"
except Exception as e:
    print e
    print "Error: unable to send email"


