#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：multi-table.py
# 输出9*9乘法口诀表
# By Droid-MAX
# Date:2017/11/25
 
for i in range(1, 10):#i控制行
    print 
    for j in range(1, i+1):#j控制列
        print "%d*%d=%d" % (i, j, i*j),