#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3543
    def toUppers(L):
        return [???]

    print toUppers(['Hello', 'world', 101])
'''

def toUppers(L):
    return [i.upper() for i in L if isinstance(i, str)]
print(toUppers(['Hello', 'world', 101]))


