#! /usr/bin/env python
# -*-coding:utf-8-*-

import requests,json

url = 'http://10.1.10.84:8080/v1.0/IvrCall/'
s = json.dumps({'key1': 'value1', 'key2': 'value2'})
r = requests.post(url, data=s)
print r.text