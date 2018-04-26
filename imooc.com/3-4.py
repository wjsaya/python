#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3267
任务:
等差数列可以定义为每一项与它的前一项的差等于一个常数，可以用变量 x1 表示等差数列的第一项，用 d 表示公差，请计算数列
1 4 7 10 13 16 19 ...
前 100 项的和。
'''

x1 = 1
d = 3
n = 100
x100 = x1 + (n-1)*d
s = (x1 + x100) * (n/2)
print(s)