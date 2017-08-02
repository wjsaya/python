#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya
#**第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os
import re

def file_list(dir):
    os.chdir(dir)
    F_list = [ F for F in os.listdir("./") if os.path.splitext(F)[1]==".py"]
    for name in F_list:
        result = word_count(name)
        print (name+"中，注释为"+str(result[0])+"行，空行为"+str(result[1])+"行，有效代码行数为"+str(result[2]))

def word_count(name):
    count = [0, 0, 0]
    #第一个为注释，第二个为空格，第三个为代码
    file = open(name, 'r', encoding="utf-8").readlines()
    for line in file:
        if re.match(r'[ ]*#', line):
            count[0] += 1
        elif re.match(r'$', line):
                count[1] += 1
        else:
            count[2] += 1
    return count

if __name__ == "__main__": 
    #dir = input("输入代码目录:")
    dir = "code"
    file_list(dir)
