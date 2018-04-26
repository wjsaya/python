#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3273
任务:
请运行如下代码，并解释打印的结果：
'''

a = 'python'
print('hello,', a or 'world')
# a or 'world'，a非空，即为True，在做or运算，所以直接返回True，即a or 'world'返回a的值：python

b = ''
print('hello,', b or 'world')
#b为空字符串，那么开始检测'world',此为True，所以返回'world'