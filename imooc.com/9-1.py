#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3537
任务:
请用for循环迭代数列 1-100 并打印出7的倍数。
'''
for i in range(1, 100):
    if i%7 == 0:
        print (i)


print ('\n'.join('%s' % i for i in range(7,101,7)))