#!/usrbin/env python3
#coding: utf-8

import requests
import sys
import io
import re
import os
import time

def get_url_list(url):
    print (url)
    return ['1','2','3','4','5']

def get_pic(i):
    print (i)
    time.sleep(1)
    return (i)

def down(one, i):
    print (one)
    print (i)

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

    url = "http://www.xxx.com"
    page_number = input("下载多少页？")
    url_list = get_url_list(url)
    count = 0 
    for i in url_list:
        if str(count) < page_number:
            one = get_pic(i)
            down(one, i)
            count += 1
            print (i+"：已经全部下载完成")
            