#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'''
python3.5+

pip3 install sanic

压测：
yum -y install httpd-tools
ab -c 30 -n 10000 http://127.0.0.1:9091/
'''

from sanic import Sanic
from sanic.log import logger
import sanic.response 

app = Sanic()

@app.route("/",methods=['POST','GET']) # 路由方式1
async def test(request):
    #logger.info('test log')
    #return sanic.response.json({"hello": "world"})
    return sanic.response.text("Hello, world")

'''
测试：
curl http://127.0.0.1:9091/test?var1=123
curl -H "Content-Type:application/json" http://127.0.0.1:9091/test -X POST --data "{\"var1\":123}"
'''
async def handler_test1(request):
    #print(dir(request))
    print(request.method)
    if request.method == "GET":
        print(request.args)
        var1 = request.args.get('var1')
        print("var1 :",var1)
    if request.method == "POST":
        print(request.json)
        print("var1 :",request.json.get("var1"))
    return sanic.response.text("test response")

if __name__ == "__main__":
    app.add_route(handler_test1, '/test',methods=['POST','GET']) # 路由方式2
    app.run(host="0.0.0.0", port=9091,debug=False, access_log=False,workers=2)


