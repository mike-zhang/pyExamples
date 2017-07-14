#! /usr/bin/env python
# -*- coding:utf-8 -*-
# version : Python 2.7.13

import psycopg2

try:
    conn = psycopg2.connect("dbname='testdb' user='testuser' host='127.0.0.1' password='pwd'")
    conn.autocommit = True
except:
    print "I am unable to connect to the database"
    
cur = conn.cursor()

cur.execute(""" 
create table students (
    id bigserial primary key,
    name varchar(20) NOT NULL  
);
""")
print "create table ok"

for i in range(10) :
    cur.execute("insert into students values (%d,'stu%d');" % (i,i))
print "insert data ok"

cur.execute("""select * from students;""")

rows = cur.fetchall()

print "\nShow me the databases:\n"
for row in rows:
    print row
           
cur.execute("""drop table students;""") 
print "drop table ok"   




    