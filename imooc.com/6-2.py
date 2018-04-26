#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3500
任务:
根据如下dict：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

请打印出：

Adam: 95
Lisa: 85
Bart: 59

'''

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}


print ('Adam: ' + str(d.get('Adam')))
print ('Lisa: ' + str(d.get('Lisa')))
print ('Bart: ' + str(d.get('Bart')))


for i,j in d.items():
    print (i + ': ' + str(j))