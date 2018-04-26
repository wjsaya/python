#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3255
任务:
月份也可以用set表示，请设计一个set并判断用户输入的月份是否有效。
月份可以用字符串'Jan', 'Feb', ...表示。
'''

months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print ('x1: ok')
else:
    print ('x1: error')

if x2 in months:
    print ('x2: ok')
else:
    print ('x2: error')