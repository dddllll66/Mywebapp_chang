import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

async def handle(request):
    name = request.match_info.get('name',"Anonymous")
    text = "Hello,  " + name
    return web.Response(text=text,content_type='text/html')

app = web.Application()
app.add_routes([web.get('/',handle),      web.get('/{name}',handle)])
logging.info('server started at http://127.0.0.1:9000...')

if __name__ =="__main__":
    web.run_app(app, host = '127.0.0.1',port = 9000)
'''写法2，用了loop
def index(request):
    return web.Response(body=b'<h1>Chang is running!</h1>',content_type='text/html')

async def init(loop):
    #把@asyncio.coroutine替换为async：标记这个generator为coroutine类型
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)#把yield from替换为await
    logging.info('server started at http://127.0.0.1:9000...')#打印出这句话
    return srv

loop = asyncio.get_event_loop()# 获取EventLoop：一个支持异步IO的消息循环模型
loop.run_until_complete(init(loop))#执行协程
loop.run_forever()
'''
