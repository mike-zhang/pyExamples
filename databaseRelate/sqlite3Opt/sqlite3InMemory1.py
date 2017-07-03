#! /usr/bin/env python 
#-*- coding:utf-8 -*- 
# version : Python 2.7.13

import sqlite3
query = """
create table test(
    id integer,
    name varchar(20)
);
"""
con = sqlite3.connect(":memory:")
con.execute(query)
con.commit()

con.execute("insert into test values(1,'name1')")
con.commit()

cursor = con.execute("select * from test")
rows = cursor.fetchall()
print rows


