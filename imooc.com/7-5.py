#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3515
任务:
汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。
我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
如果a只有一个圆盘，可以直接移动到c；
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
move(n, a, b, c)
例如，输入 move(2, 'A', 'B', 'C')，打印出：
A --> B+*-
A --> C
B --> C
'''


def move(n, a, b, c):
    '''
    函数功能：把a上面的n个方块借助b移动到c
    '''
    if n == 1:
        print (a,'-->',c)       #如果n为1，那么直接把a上的1放到c
        return None
    move(n-1, a, c, b)          # 1，递归，把a上的n-1借助c移动到b
    print (a,'-->',c)           # 2，把a上剩下的1移动到c
    move(n-1, b, a, c)          # 3，把b上的n-1借助a移动到c

move(4, '1', '2', '3')
