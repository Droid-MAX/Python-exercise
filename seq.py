#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 有四个数字：1、2、3、4，计算并输出能组成多少个互不相同且无重复数字的三位数
# 文件名：seq.py
# By Droid-MAX
# Date:2017/11/23

count=0#定义计数器
for i in range(1,5):#百位的取值范围，1<=i<5
    for j in range(1,5):#十位的取值范围，1<=i<5
        for k in range(1,5):#个位的取值范围，1<=i<5
            if( i != k ) and (i != j) and (j != k):#当个十百位上的数互不相同且无重复时，输出所有满足条件的排列
            	count+=1
                print i,j,k
print "符合条件的数有："+str(count)+" 个"#count强制类型转换为str(字符串)类型