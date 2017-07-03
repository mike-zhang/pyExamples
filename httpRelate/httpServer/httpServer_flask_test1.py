#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print "post :",request.form
    else :
        print "get :",request.args
    return 'test data!'

if __name__ == '__main__':    
    app.run(host="0.0.0.0",port=8080)
    