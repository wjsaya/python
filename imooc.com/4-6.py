#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3360
任务:
请用两种方式打印出 hello, python.
'''

L = ['Adam', 'Lisa', 'Bart']
L[0],L[1],L[2] = L[2],L[1],L[0]
print (L)