#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3544
    print [???]
    利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print([i*100 + j*10 + i for i in range(0, 10) for j in range(0, 10) if i != 0])

