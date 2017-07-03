#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import sqlite3

db=sqlite3.connect(":memory:")
c = db.cursor()

print("do create : ")
c.execute('create table tb1 (id integer,name text,score real)')
db.commit()

scores = {
(1,'test1',89.34),
(2,'test2',79.30),
(3,'test3',89.89)
}

print("do insert : ")
c.executemany('insert into tb1 values(?,?,?)',scores)
db.commit()

print("do select1 : ")
for row in db.execute('select * from tb1'):
    print(row)

min_score = 80

print("do select2 : ")
for row in db.execute('select * from tb1 where score >= ?',(min_score,)):
	print(row)
db.close()

