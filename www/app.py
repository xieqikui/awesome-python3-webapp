#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'xieqikui'

'''
编写web app框架
aiohttp模块的官方文档：https://aiohttp.readthedocs.io/en/stable/client.html
'''

import logging; logging.basicConfig(level = logging.INFO)

# import asyncio, os, json, time
import asyncio
# from datetime import datetime
from aiohttp import web

# 制作响应函数
async def index(request):
	# return web.Response(body = b'<h1>Awesome</h1>')
	return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
# web app初始化
async def init(loop):
	app = web.Application(loop=loop)	# 创建事件响应函数集合
	app.router.add_route('GET', '/', index)	# 把响应函数添加到事件响应函数集合
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9001)	# 创建服务器(连接网址、端口，绑定handler)
	logging.info('server started at http://127.0.0.1:9001...')
	return srv

loop = asyncio.get_event_loop()	# 创建事件
loop.run_until_complete(init(loop))	#  调用事件处理函数集合处理事件
loop.run_forever()