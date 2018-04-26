#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3255
任务:
zip()函数可以把两个 list 变成一个 list：
>>> zip([10, 20, 30], ['A', 'B', 'C'])
[(10, 'A'), (20, 'B'), (30, 'C')]
在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。
提示：考虑使用zip()函数和range()函数
'''

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print (index+1, '-', name)