#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3255
任务:
sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
'''

L = []
L = [i*i for i in range(1, 101)]
print (sum(L))