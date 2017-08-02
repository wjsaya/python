#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya
#第 0008 题：一个HTML文件，找出里面的正文。
import re
import os

def analyze(file_name):
    os.listdir()
    print(os.getcwd())
    line = open(file_name,'r',encoding='utf-8').read()
    print (line)
        # re.findal(r'',)

if __name__ == "__main__": 
    html = "./test.html"
    analyze(html)
