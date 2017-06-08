#coding: utf-8
#Auther: wjsaya
import re
import requests
from bs4 import BeautifulSoup
def get_soup(url):
    html = requests.get(url, headers=firefox)
    soup = BeautifulSoup(html.content.decode("utf-8"), "lxml")
    return soup

def get_urls(soup):
    li = []
    for i in soup.find_all('a'):
        li.append(i.text)
        li.append(i.get('href'))
   
    i=0
    while int(i) < 665: 
        print (i)
        print (li[i]) 
        url = "http://www.bttiantang.org"+li[i+1]
        with open ('url', 'a') as f:
            f.write(url)
            f.write('\n')
        #soup2 = get_soup("http://www.bttiantang.org"+li[i+1])
        #print (soup.find_all('a','class=download'))
        i += 4


if __name__ == "__main__":
    url = 'http://www.bttiantang.org/'
    firefox = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0 FirePHP/0.7.4"}
    soup = get_soup(url)
    get_urls(soup)

