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
    #li = []
    for i in soup.find_all('a','class=dpwnload'):
        print(i)
        #li.append(i.text)
        #li.append(i.get('href'))
#        print (i.get('href'))
   



if __name__ == "__main__":
    for line in open("url"):
        firefox = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0 FirePHP/0.7.4"}
        soup = get_soup(line)
        get_urls(soup)

