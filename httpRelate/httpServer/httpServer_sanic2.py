# run with token 
import time,json,wave,struct
import asyncio
import websockets
from sanic import Sanic
from sanic.log import logger
import sanic.response 

app = Sanic(name="test1")

settings = {
    "debug" : False ,    
}

sampleRate = 16000.0 # hertz
duration = 1.165 # seconds
frequency = 440.0 # hertz

dataPtn = '''{
    "token": "5beee3f3399af60db7ff541e8a7d174a",
    "appkey": null,
    "channel": 4,
    "modelCode": null,
    "appSecret": "sCnuN1dBjiof1hEI5g0zv",
    "fontName": "BV407_V2_streaming",
    "rate": 16000,
    "volume": 1.0,
    "speedLevel": 1.0,
    "text": "%s"
}
'''

async def send_msg(websocket,text,dstFile):
    data = dataPtn % text
    await websocket.send(data)
    fout = None 
    
    while True:
        recv_text = await websocket.recv()
        rcvType = type(recv_text)
        print(rcvType)
        mtype = ""
        if rcvType == str : 
            print(f"{recv_text}")
            msg = json.loads(recv_text)
            mtype = msg.get("messageType") or ""
        if mtype == "ttsFinish":
            fout.close()
            break
        if mtype == "ttsStart":
            fout = wave.open(dstFile,'w') 
            fout.setnchannels(1) # mono
            fout.setsampwidth(2)
            fout.setframerate(sampleRate)
        if rcvType == bytes :
            fout.writeframesraw( recv_text )    

async def main_logic():
    async with websockets.connect('ws://10.130.118.118:9093/tts') as ws:
        await send_msg(ws,"今天天气不错","1.wav")

@app.route("/",methods=['POST','GET']) # 路由方式1
async def get(request):
    #logger.info('test log')
    #return sanic.response.json({"hello": "world"})
    #return sanic.response.text("Hello, world")

    tmpFile = "1.wav" 
    text = request.args.get('text').strip()
    print("text : %s" % text)
    if len(text) > 0 :
        #asyncio.get_event_loop().run_until_complete(main_logic())    
        await main_logic()
        #async with websockets.connect('ws://10.130.118.118:9093/tts') as ws:
        #    await send_msg(ws,text,tmpFile)
        
        '''
        self.set_header('content-type', 'audio/mpeg')
        fbin = open(tmpFile,"rb").read()
        self.set_header('Content-Length', len(fbin))
        self.set_header('Content-Disposition', 'attachment;filename="%s"'%tmpFile)
        self.write(fbin)
        self.finish()            
        '''
        
        return await sanic.response.file_stream(
            tmpFile,
            chunk_size=1024,
            mime_type="audio/mpeg",
            headers={
                "Content-Disposition": 'Attachment; filename="1.wav"',
                "Content-Type": "audio/mpeg",
            },
            )
        
    else:
        pass 
        #self.set_header('content-type', 'application/json')
        #self.finish(json.dumps({"result" : "input text "}))    
    return sanic.response.text("Hello, world")

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
    app.add_route(handler_test1,'/test',methods=['POST','GET']) # 路由方式2
    app.run(host="0.0.0.0", port=8091,debug=False, access_log=False,workers=2)
    
'''    

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        tmpFile = "1.wav" 
        print("get",self.request.arguments)
        text = self.get_query_argument("text").strip()
        print("text : %s" % text)
        if len(text) > 0 :
            #text2File(text,tmpFile)
            await text2File(text,tmpFile)
            self.set_header('content-type', 'audio/mpeg')
            fbin = open(tmpFile,"rb").read()
            self.set_header('Content-Length', len(fbin))
            self.set_header('Content-Disposition', 'attachment;filename="%s"'%tmpFile)
            self.write(fbin)
            self.finish()            
        else:
            self.set_header('content-type', 'application/json')
            self.finish(json.dumps({"result" : "input text "}))
        
    async def post(self):
        print("post")
        print(self.request.arguments)

if __name__ == "__main__":
    port = 8091
    print("listen on port %d"%port)
    application = tornado.web.Application([
        (r"/", MainHandler),
    ],**settings)
    
    application.listen(port)    
    tornado.ioloop.IOLoop.instance().start()
    
'''
    