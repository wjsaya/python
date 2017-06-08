#coding: utf-8
#Auther: wjsaya
import re
import requests
from bs4 import BeautifulSoup
def get_soup(url):
    try:
        html = requests.get(url, headers=firefox)
    except Exception:
        print (Exception)
    try:
        soup = BeautifulSoup(html.content.decode("utf-8"), "lxml")
    except Exception:
        print (Exception)
    return soup

def get_urls(soup, url, name):
    li = []
    L = soup.find_all("div", class_="dl_item")
    for i in range(1,len(L)):
        for l in L[i].find_all('a', class_='download'):
            url.append("http://www.bttiantang.org/"+l['href'])
        for l in  L[i].find('div', class_="dl_item_cell dl_item_cell_note"):
            name.append(l) 
   
def get_magents(url, name):
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
        


if __name__ == "__main__":
        #file = open("./url", "r")
        for line in open("url"):
            firefox = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0 FirePHP/0.7.4"}
            soup = get_soup(line)
            url = []
            name = []
            get_urls(soup, url, name)
            get_magents(url, name)
