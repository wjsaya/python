#coding: utf-8
import re
import requests
from bs4 import BeautifulSoup

url = "https://music.douban.com/top250?start=25"
firefox={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0 FirePHP/0.7.4"}

def main():
    maxm = input("想获取豆瓣排名前多少的音乐列表呢？(0-250之间）：")
    count_main = 0
    url_li = get_pages()
    for i in range(0,9):
        if count_main < int(maxm):
            count_main += get_details(url_li[i], count_main, maxm)


def get_soup(url):
    html = requests.get(url, headers=firefox)
    soup = BeautifulSoup(html.content, 'lxml')
    return soup


def get_details(url, count_in_loop, maxm):
    content = get_soup(url)
    html = content.find_all('a', class_="nbg")
    for i in range(0,25):
        if count_in_loop < int(maxm):
            print ("歌手-名字："+html[i]["title"])
            print ("链接："+html[i]["href"])
        count_in_loop += 1
    return count_in_loop

def get_pages():
    content = get_soup(url)
    l = content.find("div", class_="paginator")
    url_li = []
    for i in l.find_all('a'):
        url_li.append(i['href'])
    return url_li[0:9]

if __name__ == '__main__':
    main()
