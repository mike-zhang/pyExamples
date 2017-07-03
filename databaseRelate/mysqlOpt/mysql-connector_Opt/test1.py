#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',password='',
    database='test',use_unicode=True
)
cursor = conn.cursor()

cursor.execute('drop table if exists `user`;')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20));')

cursor.execute('insert into user (id, name) values ("2", "Mike")')
print cursor.rowcount

conn.commit()

cursor.execute('select * from user ')
values = cursor.fetchall()
print values

cursor.close()


