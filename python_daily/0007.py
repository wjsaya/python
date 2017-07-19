#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya
#**第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

def file_list(dir):
    os.chdir(dir)
    for root, dir, F_list in os.walk("./"):
        for name in F_list:
            print (name)
            word_count(name)


def word_count(name):
    file = open(name, 'r', encoding="utf-8")
    print (file)

if __name__ == "__main__": 
    dir = input("输入代码目录:")
    file_list(dir)
