#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3255
任务:
给定一个dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
请计算所有同学的平均分。
'''

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for score in d.values():
    sum += score
print (sum/len(d))