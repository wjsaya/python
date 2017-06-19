#coding: utf-8
#Auther: wjsaya
#**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

def file_open(filename):
    f = open(filename, 'r').read()
    #打开文件
    ff = re.findall('([a-zA-Z0-9]+)', f)
    #正则匹配，组内为大小写字母加数字，后面限定位数为一位以上
    print (ff)
    print (len(ff))

if __name__ == "__main__":
    file = input("将要统计的文件为:")
    file_open(file)
