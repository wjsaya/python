#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3363
任务:
由于 t 包含一个list元素，导致tuple的内容是可变的。能否修改上述代码，让tuple内容不可变？
t = ('a', 'b', ['A', 'B'])
print (t)
'''

t = ('a', 'b', ('A', 'B'))
print (t)