#! /usr/bin/env python
#-*- coding : utf-8 -*-

rows = [
    {"id" : 1001,'name': "user1","score" : 80},
    {"id" : 1002,'name': "user8","score" : 60},
    {"id" : 1003,'name': "user7","score" : 70},
    {"id" : 1004,'name': "user6","score" : 90},
    {"id" : 1005,'name': "user3","score" : 99},
    {"id" : 1006,'name': "user5","score" : 66}, 
]

def show(rows):    
    for item in rows :
        print item
    print("-" * 50)

show(rows)

rows_byname2 = sorted(rows, key=lambda x:x["score"])  
show(rows_byname2)
