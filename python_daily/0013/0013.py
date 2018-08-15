#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-15 23:55:53 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-16 02:10:36 
import os
import requests
from lxml import etree

head = {
    "Host" : "tieba.baidu.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding" : "gzip, deflate"
}

def main():
    '''主函數 \n
    下载的帖子预览图在pic目录 \n
    高清图在picBig目录 \n
    '''
    createDir("pic")
    createDir("picBig")
    rsp = requests.get("http://tieba.baidu.com/p/2166231880?traceid=", headers=head).content.decode('utf-8')
    a = etree.HTML(rsp)
    rsp = a.xpath("//img[@class='BDE_Image']/@src")
    for url in rsp:
        get_pic(url)
        get_big_pic(url)


def get_pic(url):
    '''下载预览图
    '''
    head['host'] = "imgsrc.baidu.com"
    fileName = "./pic/" + url.split("=")[1].split("/")[1]
    rsp = requests.get(url, headers=head).content
    with open (fileName, 'wb') as f:
        f.write(rsp)


def get_big_pic(url):
    '''下载高清图
    '''
    head['host'] = "imgsrc.baidu.com"
    id = url.split("=")[1].split("/")[1][:-4]
    fileName = "./picBig/" + id + ".jpg"
    fileUrl = "http://imgsrc.baidu.com/forum/pic/item/" + id + ".jpg"
    rsp = requests.get(fileUrl, headers=head).content
    with open (fileName, 'wb') as f:
        f.write(rsp)
    

def createDir(dirName):
    '''传入目录 \n
    目录不存在，创建之 \n
    存在，删除其下所有文件 \n
    '''
    if dirName not in os.listdir():
        os.mkdir(dirName)
    else:
        for i in os.listdir(dirName):
            fileName =  ".\\" + dirName + "\\" + i 
            os.remove(fileName)


main()


