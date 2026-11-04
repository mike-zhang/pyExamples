#! /usr/bin/env python3
#-*- coding:utf-8 -*- 

import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

settings = {
    "debug" : False ,    
}
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("get")
        print(self.request.arguments)
        #query = self.get_query_argument("query")
        #print("query : %s" % query)
        self.set_header('content-type', 'application/json')
        #self.write(json.dumps({"result" : "test message"}))
        self.finish(json.dumps({"result" : "test message"}))

    '''
    # async 
    @tornado.gen.coroutine
    def get(self):
        print("get")
        self.set_header('content-type', 'application/json')
        yield self.finish(json.dumps({"result" : "test message"}))
    '''  
        
    def post(self):
        print("post")
        print(self.request.arguments)

if __name__ == "__main__":
    port = 8091
    print("listen on port %d"%port)
    application = tornado.web.Application([
        (r"/", MainHandler),
    ],**settings)
    
    application.listen(port)
    
    #http_server = tornado.httpserver.HTTPServer(application)
    #http_server.bind(port,"0.0.0.0")
    #http_server.start(num_processes=0) # tornado将按照cpu核数来fork进程
    
    tornado.ioloop.IOLoop.instance().start()
    