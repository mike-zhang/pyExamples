#! /usr/bin/env python
# -*-coding:utf-8-*-

import requests

url = 'http://127.0.0.1:4567'
files = {'file': open('img1.jpg','rb')}
values = {'author': 'Mike Zhang'}
r = requests.post(url, files=files,data=values)

