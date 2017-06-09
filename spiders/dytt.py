#coding: utf-8
#Auther: wjsaya
import re
import requests
from bs4 import BeautifulSoup

def get_soup(url):
#函数，获取url的信息并转换为soup
    try:
        html = requests.get(url, headers=firefox)
    except Exception:
        print ("无法打开"+url)
    else:
        soup = BeautifulSoup(html.content.decode("utf-8"), "lxml")
        return soup

def get_page_urls(soup):
#获取电影对应的详情页
    li = []
    for i in soup.find_all('a'):
        li.append(i.text)
        li.append(i.get('href'))
    i=0
    while int(i) < 665: 
        url = "http://www.bttiantang.org"+li[i+1]
        get_download_link(url)
        i += 4

def get_link_urls(soup, url, name):
#从电影详情页获取下载链接
    li = []
    try:
        L = soup.find_all("div", class_="dl_item")
    except Exception:
        print ("未找到div")
    else:
        for i in range(1,len(L)):
            for l in L[i].find_all('a', class_='download'):
                url.append("http://www.bttiantang.org/"+l['href'])
            for l in  L[i].find('div', class_="dl_item_cell dl_item_cell_note"):
                name.append(l) 

def get_magents(url, name):
#从下载链接获取磁力链接
    for i in range(0,len(url)):
        print (name[i])
        with open ("./movies", 'a') as f:
            f.write(name[i]+"\n")
        soup = get_soup(url[i])
        magent = soup.find_all('a', title="不能下载？点此从备用服务器下载")
        for i in magent:
            print (i['href'])
        with open ("./movies", 'a') as f:
            f.write(i['href']+"\n")
        with open ("./movies", 'a') as f:
            f.write("------------------------------------------------------------------\n")
        

def get_download_link(downloadurl):
#获取电影下载链接
    soup = get_soup(downloadurl)
    url = []
    name = []
    get_link_urls(soup, url, name)
    get_magents(url, name)


if __name__ == "__main__":
    url = 'http://www.bttiantang.org/'
    firefox = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0 FirePHP/0.7.4"}
    soup = get_soup(url)
    get_page_urls(soup)
