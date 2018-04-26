#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3536
任务:
字符串有个方法 upper() 可以把字符变成大写字母：
>>> 'abc'.upper()
'ABC'
但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
提示：利用切片操作简化字符串操作。
'''

def firstCharUpper(s):
    return s[0].upper() + s[1:]
    #return s.title()
    #return s.capitalize()

print(firstCharUpper('hello'))
print(firstCharUpper('sunday'))
print(firstCharUpper('september'))