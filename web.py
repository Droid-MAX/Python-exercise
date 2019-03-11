#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：web.py
# 使用Bottle框架做一个简单的HelloPython
# By Droid-MAX
# Date:2017/12/6

from bottle import route, run
#导入Bottle框架的route和run组件用于路由映射和运行web应用

@route('/')
def hello():
	return "Hello Python!"
#将URL与hello函数进行绑定，函数将会映射到URL地址上

run(host='0.0.0.0', port=8080, reloader=True)
#运行web应用在http://0.0.0.0:8080/
#reloader=True开启自动重载