#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3425
任务:
利用while循环计算100以内奇数的和。
'''
sum = 0
x = 1
while x < 100:
if x%2:
	#x%2余1，即为True，累加。余0，False，跳过
	sum += x
	x += 1
print(sum)
