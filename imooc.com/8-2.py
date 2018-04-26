#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3255
任务:
利用倒序切片对 1 - 100 的数列取出：
* 最后10个数；
* 最后10个5的倍数。
'''

[91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


L = range(1, 101)
print (L[-10:])
print (L[4::5][-10:])