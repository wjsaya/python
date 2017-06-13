#coding: utf-8
#Auther: wjsaya
import requests
from bs4 import BeautifulSoup
import re

def get_file(url, name):
    DownUrl = "http://www.chinaskills-jsw.org"+url
    try:
        html = requests.get(DownUrl)
    except Exception:
        print (Exception)
    else:
        print ("准备开始下载{"+name+"}url为：{"+DownUrl+"}")
        with open ("chinaskills/"+name, 'wb') as f:
            f.write(html.content) 

if __name__ == "__main__":
    url = "http://www.chinaskills-jsw.org/content.jsp?id=ff8080815bf9bc00015c483769e20107&classid=ff8080814ead5a97015217ea88d208a8"
    html = requests.get(url)
    content = BeautifulSoup(html.content, 'lxml')
    for i in content.find_all('a'):
        url =i['href']
        name = i.text
        get_file(url, name)



