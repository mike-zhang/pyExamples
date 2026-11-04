import tornado.ioloop
import tornado.web
import tornado.options

gNum = 0
tornado.options.parse_command_line()
class HandlerBase(tornado.web.RequestHandler):
    def genResult(self):
        pass
        
    def get(self):        
        self.genResult()
        return None            
        
    def post(self):                
        self.genResult()
        return None            

class MainHandler(HandlerBase):
    def genResult(self):        
        global gNum
        if gNum % 2 == 0 :
            self.write("yes")
        else :
            self.write("no")
        gNum += 1
        
        return None
        
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = 8091
    print("listen on port %d"%port)
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    