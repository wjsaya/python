#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3534
任务:
range()函数可以创建一个数列：
>>> range(1, 101)
[1, 2, 3, ..., 100]
请利用切片，取出：
1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。
'''

L = range(1, 101)

print (L[:10])
print (L[2::3])
print (L[4:50:5])
