#coding: utf-8
import re
import os
import requests
from bs4 import BeautifulSoup

url = 'http://jandan.net/ooxx'
page = 1
#想下载多少页？
head={
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0 FirePHP/0.7.4"
}

def get_page_num(url):
    html = requests.get(url, headers=head)
    content = BeautifulSoup(html.content.decode("utf-8"), "lxml")
    current_num_string = content.find("span",class_="current-comment-page")
    for i in current_num_string:
        q = re.findall(r'[0-9][0-9][0-9]',i)
        return q[0]
 

def get_img(url,floder):
    html = requests.get(url, headers=head)
    content = BeautifulSoup(html.content.decode("utf-8"), "lxml")
    #print (content)
    img_url = content.find_all('a',class_="view_img_link")
    for i in img_url:
        img_name = i["href"][23:]
        img_download_url = "http://"+i["href"][2:]
        img_code = requests.get(img_download_url, headers=head)
        with open ("./meizitu/"+floder+"/"+img_name, 'wb') as f:
            f.write(img_code.content)
        print (img_name+" is downloaded")

        

def get_html (url,page):
    current_page = get_page_num(url)
    while (page) > 0:
        page -= 1
        P = int(current_page)-page
        img_url = "http://jandan.net/ooxx/page-"+str(P)+"#comments"
        #拼接出所需url
        floder = str(P)
        print (floder)
        os.mkdir("./meizitu/"+floder)
        get_img(img_url,floder)

get_html (url,page)
