#/usr/bin/env python3
#coding: utf-8
'''
Date:2017-07-26
题型类型：Python爬虫练习
题目要求： 爬取小说《冰与火之歌》的1-5季内容并保存到本地。 （保存完别删，周六的时候会用到）
'''
import requests
import re

class analyze(object):
    def __init__(self, url):
        self.__url = url

#    def tu(self):
#        self.tu_url_R = (r'^.*img src="(.*)" alt.*')
#        self.tu_name_R = (r'.*alt="(.*)"[/ ]*/>.*')
#        print (base_url+re.findall(self.tu_url_R, self.__url)[0])
#        print (re.findall(self.tu_name_R, self.__url)[0])

    def chapter(self):
        self.each_url_R = (r'.*href="(.*)" class="text".*')
        self.each_name_R = (r'.*"_blank" >(.*)</a>.*')
        each_url = base_url+re.findall(self.each_url_R, self.__url)[0]
        each_url_name = re.findall(self.each_name_R, self.__url)[0]
        return (each_url_name, each_url)
#    def get_content(self):


def get_book_list(book_url):
#返回列表，为当前页下包含小说的li标签
    html = requests.get(book_url).content.decode('gbk')
    options = (r'<li>.*class="ablum".*</li>')
    return re.findall(options, html)

def get_details(list):
    for url in list:
        #print (url)
        this = analyze(url)
        #this.tu()
        print (this.chapter())
        print ("done######################################################")


if __name__ == '__main__':
    base_url ="http://www.sbkk88.com"
    books_url = 'http://www.sbkk88.com/mingzhu/waiguowenxuemingzhu/bingyuhuozhige/'
    #books_url = 'http://www.sbkk88.com/mingzhu/gudaicn/sidamingzhu/'
    book_list = get_book_list(books_url)
    get_details(book_list)

