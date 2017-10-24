#!/usr/bin/env python3
# coding: utf-8
# version: v1.0
# 添加多进程下载

import requests
import re
import os
from multiprocessing import Pool

def get_url_list(url):
    # 传入all页面的url，获取其他的所有文章链接，如下：
    #<a href="http://www.mzitu.com/99009" target="_blank">********</a>
    text = requests.get(url, headers=head).text
    R = (r'.*(http://www.mzitu.com/[0-9]+)".*')
#    print (text)
    print("从" + url + "获取专辑列表完成，开始获取页面url...")
    return re.findall(R, text)


def get_pic(url):
    # 传入一个起始图片页面url，获取其他的所有图片页面url，如下：
    #<a href="http://www.mzitu.com/98966/2"><span>2</span></a>
    #    print ("获取页面url完成，开始获取图片url并下载...")
    q = requests.get(url, headers=head).text
    title_R = (r'<h2.*title">(.*)</h2>')
    title = re.findall(title_R, q)[0]
    page_R = (r'<span>(..)</span>')
    max_page = re.findall(page_R, q)[0]
    # title是网页标题，可能含有特殊字符，需过滤
    title = re.sub(u'[\/:*?">|< 满]+', "#", title)
    return (title, max_page)


def change_dir(where):
    try:
        os.chdir(where)
    except:
        os.mkdir(where)
        os.chdir(where)
        print("创建并切换到目录'" + where + "'完成")
#    print ("切换目录到'"+where+"'完成")

    
def down(pics, url):
    # 传入一个包含图片的页面url，获取里面的图片地址并下载到本地，如下：
    #<img src="http://i.meizitu.net/2017/07/30a01.jpg" alt="**************">
    title = pics[0]
    max_page = pics[1]
    R = (r'<img src="(.*)" alt=".*>')
    origon_dir = os.getcwd()+"\\"
    change_dir('./mzitu')
    print (os.getcwd())
    current_dir = os.getcwd()+"\\"

    try:
        os.chdir(current_dir + title)
        print("'" + title + "'已下载，跳过")
    except:
        change_dir(current_dir + title)
        for i in range(0, int(max_page)):
            page = url + "/" + str(i + 1)
            html = requests.get(page, headers=head).text
            img_url = re.findall(R, html)[0]
            Multi = Pool(8)
            Multi.apply_async(download, args=(img_url, i, head, current_dir + title + "\\"))
            #change_dir("../")
            Multi.close()
            Multi.join()
            change_dir(origon_dir)

def download(img_url, i, head, current_dir):
        print (img_url+"已下载")
        pic = requests.get(img_url, headers=head)
        #print (pic)
        with open(current_dir + str(i) + '.jpg', 'wb') as f:
            for p in pic:
                f.write(p)



if __name__ == "__main__":
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Referer': 'http://www.mzitu.com/37288/3'}
    url = 'http://www.mzitu.com/all'
    page_number = input("下载多少页？")
    #page_number = "2"
    #print("#" + page_number + "#")
    url_list = get_url_list(url)
    count = 0
 #   Multi = Pool(4)
    for i in url_list:
        if str(count) < page_number:
            pics = get_pic(i)
            down(pics, i)
      #      Multi.apply(down, args=(pics, i,))
            count += 1
            print(i + "：已经全部下载完成")

  #  Multi.close()
   # Multi.join()

