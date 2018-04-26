#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3514
任务:
一元二次方程的定义是：ax² + bx + c = 0
请编写一个函数，返回一元二次方程的两个解。
注意：Python的math包提供了sqrt()函数用于计算平方根。
'''

import math

def quadratic_equation(a, b, c):
    x = b*b - 4*a*c
    if x < 0:
        return None
    elif x == 0:
        return -b / (2 *a)
    else:
        return ((math.sqrt(x) - b ) / (2 * a)) , ((-math.sqrt(x) - b ) / (2 * a))

print (quadratic_equation(2, 3, 0))
print (quadratic_equation(1, -6, 5))