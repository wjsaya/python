#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3516
任务:
请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
'''

def greet(t = 'world'):
    print ('hello,', t, '.')

greet()
greet('Bart')
