#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3513
任务:
请用两种方式打印出 hello, python.
'''

def square_of_sum(L):
    return sum([i*i for i in L])


print (square_of_sum([1, 2, 3, 4, 5]))
print (square_of_sum([-5, 0, 5, 15, 25]))