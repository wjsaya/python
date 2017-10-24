#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya
#第009题，一个HTML文件，找出里面的链接。
import re
import os


def analyze(file_name):
    #print (os.listdir())
    print (os.getcwd())
    line = open(file_name,'r',encoding='utf-8').read()
    R = (r'([hftps]+://[^\s]*)"')
    for i in  (re.findall(R, line)):
        print (i)
if __name__ == "__main__": 
    html = "./test.html"
    analyze(html)
