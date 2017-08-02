#!/bin/env python3
#coding: utf-8
import re
import requests
from bs4 import BeautifulSoup
url = 'http://bbs.wot.kongzhong.com'

data={
    "username":"1334306549@qq.com",
    "password":"123qweASDkz"}
firefox={
    "Host":"bbs.wot.kongzhong.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cookie":"Hm_lvt_8b576bd69b006b4bd46c467a87779627=1498441061",
    "Connection":"close",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"15"}
    
print (requests.get(url,headers=firefox).content.decode("utf-8"))




print (requests.get(url,data=data,headers=firefox).content.decode("utf-8"))