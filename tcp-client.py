#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：tcp-client.py
# By Droid-MAX
# Date:2017/12/6

import socket

target_host= "127.0.0.1"
target_port= 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
response = client.recv(4096)

print response