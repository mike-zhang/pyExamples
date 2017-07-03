#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

import urllib

f=urllib.urlopen("http://127.0.0.1:8080")
s=f.read()
print s

params = urllib.urlencode({'id': 1, 'name': 'mike'})
f = urllib.urlopen("http://127.0.0.1:8080?%s" % params)
print f.read()
