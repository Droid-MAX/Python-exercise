#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：sort.py
# 分别输入三个整数，由大到小输出
# By Droid-MAX
# Date:2017/11/25
 
l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l