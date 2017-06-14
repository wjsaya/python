#coding: utf-8
import time
import re
import os
import requests
from bs4 import BeautifulSoup

url = 'http://jandan.net/ooxx'
firefox = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0 FirePHP/0.7.4"}
Pg_count = input("请输入想要获取的页数(直接回车默认页码为1):")
if Pg_count == "":
    Pg_count = "1"
Pg_count=int(Pg_count)-1
#给get_html函数使用，预先+1上去，这样-1就是当前第一页。

def get_content(url):
#获取url，返回BS解析之后的content
    html = requests.get(url, headers=firefox)
    content = BeautifulSoup(html.content, "lxml")
    return content

def get_current_page(content):
#获取url，返回url中的current-comment-page（即页码）
    page_swap1 = content.find('span',class_="current-comment-page")
    page_swap2 = str(page_swap1)
    current_page = page_swap2[36:39]
    #current_page = str(content.find('span',class_="current-comment-page"))[36:39]
    #此处本来是写成了一句语句直接提取，后来想了想，万一以后想再看下，这会把自己绕晕，于是乎拆分了、、、
    return current_page

def get_img_url(content, max_page):
#获取解码后的html文件以及最大页码。获取html中的图片img_url，然后把img_url和最大页码传递给get_img函数。
    #html = BeautifulSoup(content, "lxml")
    img_li = content.find_all("a", class_="view_img_link")
    for i in img_li:
        img_url = "http:"+i["href"]
        #img_url = "http://"+i["href"].strip("/")
        get_img(img_url, max_page)
        #strip,用来删除某字符
        #并且加上http协议头
        
def get_img(img_url, floder):
#获取img_url和文件夹名（即当前网页页码），通过img_url下载图片并保存在floder内。
    img_name = img_url[28:]
    img_file = requests.get(img_url, headers=firefox)
    q = img_file.content
    with open ("./get/"+floder+"/"+img_name, 'wb') as img_file:
        img_file.write(q)
        print (floder+"/"+img_name+" is downloaded")
    
def get_html(max_page, Pg_count):
#获取最大页码数及想要下载图片的页数，循环得出每页的url地址。
    #http://jandan.net/ooxx/page-107#comments
    while Pg_count >= 0:
        pg = int(max_page)-Pg_count
        url = "http://jandan.net/ooxx/page-"+str(pg)+"#comments"
        print ("当前获取到的包含图片的页面url地址为："+url)
        Pg_count -= 1
        content = get_content(url)
        print ("开始创建图片存放目录并获取图片链接地址......")
        if os.path.exists("./get/") == False:
            os.mkdir ("./get/")
        if os.path.exists("./get/"+str(pg)) == False:
            os.mkdir ("./get/"+str(pg))
        print ("开始下载图片，本地存放目录为：./get/"+str(pg))
        time.sleep(3)
        get_img_url(content, str(pg))
    
def main():
#主函数，一切的开端
    content = get_content(url)
    current_page = get_current_page(content)
    get_html(current_page, int(Pg_count))
    

if __name__ == '__main__':
    main()

