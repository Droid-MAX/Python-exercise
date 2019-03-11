#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：fib-seq.py
# 斐波那契数列
# By Droid-MAX
# Date:2017/11/25
 
def fib(n):#定义fib函数
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
 
# 输出前 10 个斐波那契数列
print fib(10)