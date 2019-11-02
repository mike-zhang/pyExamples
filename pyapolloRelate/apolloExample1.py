#! /usr/bin/env python3
#-*- coding:utf-8 -*- 

import pyapollo

a = pyapollo.ApolloClient("test1","default","http://192.168.1.100:8080")
a.start()

for key in ["ip","port"]:
	v = a.get_value(key)
	print("%s : " % key)
	print(v)