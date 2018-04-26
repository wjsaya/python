#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3507
任务:
请用 for 循环遍历如下的set，打印出 name: score 来。
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
'''

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print (x[0]+':', x[1])