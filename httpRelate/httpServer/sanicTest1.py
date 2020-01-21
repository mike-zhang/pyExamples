#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'''
python3.5+

pip3 install sanic

压测：
yum -y install httpd-tools
ab -c 30 -n 10000 http://127.0.0.1:9093/
'''
from sanic import Sanic
from sanic.response import text

app = Sanic()

@app.route("/",methods=['POST','GET']) 
async def test(request):
    return text("Hello, world")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9093,debug=False, access_log=False,workers=2)

