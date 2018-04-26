#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3428
任务:
对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
'''

for x in range(1, 10):
    for y in range(x+1, 10):
        print (x*10 + y)