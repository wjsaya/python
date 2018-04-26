#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3255
任务:
请用 for 循环遍历如下的dict，打印出 name: score 来。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
'''

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

for i,j in d.items():
    print ("%s: %s" % (i, j))

for i in d:
    print (i + ':', d[i])