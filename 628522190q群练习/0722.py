#/usr/bin/env python3
#coding: utf-8
'''
Date:2017-07-22
题型类型：Python语法练习
题目要求： 统计一篇英文文章中所有单词的出现次数
测试文章： LeEco in deep water after failing to meet debt payment deadline(http://www.globaltimes.cn/content/1057467.shtml)
'''

import re

def To_Array(line):
    rr = '[a-zA-Z0-9]+'

    return re.findall(rr, line)
    
def Count(array_count):
    dict_count = {"":""}

    for word in array_count:
        if dict_count.get(word) is None:
            counter = 0
        else:
            counter = dict_count.get(word)
        dict_count[word] =counter + 1
    return (dict_count)

if __name__ == '__main__':
    file_line = open("./0722_file", 'r',).readlines(h)
    print (file_line)
    array_file = To_Array(file_line)
    array_result = Count (array_file)
    print (array_result)