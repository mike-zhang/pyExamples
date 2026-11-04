#! /usr/bin/env python3
# -*-coding:utf-8-*-

import requests

url = "http://127.0.0.1:8080/test1"
headers = {
    "Content-Type":"application/json",
    "charset":"UTF-8"
}
r = requests.get(url,headers = headers)
#print dir(r)
print(r.text)

