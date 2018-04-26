#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3423
任务:
如果按照分数划定结果：
    90分或以上：excellent
    80分或以上：good
    60分或以上：passed
    60分以下：failed
'''
score = 85
if score >= 90:
    print ('excellent')
elif score >= 80:
    print ('good')
elif score >= 60:
    print ('passed')
else:
    print ('failed')