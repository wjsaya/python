#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3517
任务:
请编写接受可变参数的 average() 函数。
'''

def average(*args):
    if not len(args):
        return 0.0
    return (1.0*sum(args)/len(args))

print (average())
print (average(1, 2))
print (average(1, 2, 2, 3, 4))