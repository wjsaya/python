#coding: utf-8
#Auther: wjsaya
import requests
from bs4 import BeautifulSoup
import re
def get_name_url(url, headers):
    html = requests.get(url, headers=headers)
    content = BeautifulSoup(html.content, 'lxml')
    for i in content.find_all('a'):
        url =i['href']
        name = i.text
        if re.findall(r'.*赛项.*', name) != []:
            get_file(url, name)

def get_file(url, name):
    DownUrl = "http://www.chinaskills-jsw.org"+url
    try:
        print ("qqq")
   #     html = requests.get(DownUrl)
    except Exception:
        print (Exception)
    else:
        print ("正在下载:"+name)
        #with open ("chinaskills/"+name, 'wb') as f:
        #    f.write(html.content) 

if __name__ == "__main__":
    url = "http://www.chinaskills-jsw.org/content.jsp?id=ff8080815bf9bc00015c483769e20107&classid=ff8080814ead5a97015217ea88d208a8"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0 FirePHP/0.7.4"}
    get_name_url(url, headers)
