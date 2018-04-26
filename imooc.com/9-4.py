#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3540
任务:
请根据dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
打印出 name : score，最后再打印出平均分 average : score。
'''

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print (k,':', v)
print ('average', ':', sum/len(d))