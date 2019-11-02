#! /usr/bine/env python3
#-*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado

settings = {
    "debug" : False ,
}

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],**settings)

if __name__ == "__main__":
    app = make_app()
    port = 9093
    #app.listen(port)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(port,"0.0.0.0")
    http_server.start(num_processes=2)

    tornado.ioloop.IOLoop.current().start()

