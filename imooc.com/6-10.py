#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3508
任务:
针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
'''

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for i in L:
    try:
        s.remove(i)
    except KeyError:
        s.add(i)

print (s)