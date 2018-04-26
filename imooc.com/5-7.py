#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3427
任务:
对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
    sum = 0
    x = 1
    while True:
        sum = sum + x
        x = x + 1
        if x > 100:
            break
    print sum
    #题目原始待修改代码如下：
    sum = 0
    x = ?
    while True:
        x = x + 1
        if x > 100:
            break
        ???
    print sum
'''

sum = 0
x = 0               #循环先执行x++，所以x初始必须为0，这样x++初始为1，符合题目要求 
while True:
    x = x + 1
    if x > 100:
        break
    if not x%2:     #如果x%2不为真(余为1)，continue
        continue
    sum += x
    
print (sum)