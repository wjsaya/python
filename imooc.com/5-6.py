#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3426
任务:
利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
'''

#临时变量x，用来获取2^n-1
sum = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    sum += x
    x *= 2
    n += 1
print (sum)

#直接调用pow()函数
sum = 0
n = 1
while True:
    if n > 20:
        break
    sum += pow(2,n-1)
    n += 1
print (sum)