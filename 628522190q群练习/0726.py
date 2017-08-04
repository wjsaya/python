#/usr/bin/env python3
#coding: utf-8
# version: v1.0
'''
Date:2017-07-26
题型类型：Python爬虫练习
题目要求： 爬取小说《冰与火之歌》的1-5季内容并保存到本地。 （保存完别删，周六的时候会用到）
'''
import os
import re
import time
import requests


def change_dir(where):
    try:
        os.chdir(where)
    except:
        os.mkdir(where)
        os.chdir(where)
        print("创建并切换到目录'" + where + "'完成")
#    print ("切换目录到'"+where+"'完成")


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
    def get_page_url(self):
        time.sleep(0.5)
        #print (self.__url)
        name_list = []
        url_list = []
        #print (self.__url)
        html = requests.get(self.__url).content.decode("gbk")
        self.each_name_R = (r' <li> <a href=(.*).*</a> </li>')
        each_url_name = re.findall(self.each_name_R, html)
        each_url_name = each_url_name[0].replace('<li> <a href=','\r\n')
        each_url_name = each_url_name.replace(' class="articleTitle"  target="_blank">','')
        each_url_name = each_url_name.replace('</a> </li>','')
        each_url_names = each_url_name.split('"')
        #print (len(each_url_name))
        for i in range(1, len(each_url_names)):
            if (i % 2) == 0:
                name_list.append(each_url_names[i])
            else:
                url_list.append(each_url_names[i])
        time.sleep(5)
        self.download(name_list, url_list)
        
    def download(self, name_list, url_list):
        for i in range(0,len(name_list)):
            print (name_list[i],url_list[i])
            count = 0
            base_url ="http://www.sbkk88.com"
            file_name = name_list[i]
            url = url_list[i]
            options = (r'(<p>.*</p>)')
            html = requests.get(base_url+url).content.decode("gbk")
            temp =  (re.findall(options, html))
            #print (temp)
            for i in range(0,len(temp)):
                count += 1
                if (count %10) == 0:
                    time.sleep(2)
                lines = temp[i]
                lines = lines.replace('<u>一</u>','')
                lines = lines.replace('<p>','')
                lines = lines.replace('</p>','\n')
                file_name  = file_name.replace('\r\n', '')
                with open('./'+file_name, 'a') as f:
                    f.write(lines)



            
        
#<a href="/mingzhu/waiguowenxuemingzhu/bingyuhuozhige/b1/145664.html" class="articleTitle" target="_blank">卷1：权力的游戏 Chapter1 序曲</a>


def get_book_list(book_url):
#返回列表，为当前页下包含小说的li标签
    html = requests.get(book_url).content.decode('gbk')
    options = (r'<li>.*class="ablum".*</li>')
    return re.findall(options, html)

def get_chapters(list):
    name_list = []
    url_list = []
    for url in list:
        #print (url)
        this = analyze(url)
        #this.tu()
        name_list.append(this.chapter()[0])
        url_list.append(this.chapter()[1])
    return (name_list, url_list)

def download(chapters):
    names = chapters[0]
    urls = chapters[1]
    for count in range(0, len(names)):
        change_dir('./小说下载')
        change_dir(names[count])
        pic = analyze(urls[count])
        pic.get_page_url()
        change_dir('../../')
    


if __name__ == '__main__':
    base_url ="http://www.sbkk88.com"
    books_url = 'http://www.sbkk88.com/mingzhu/waiguowenxuemingzhu/bingyuhuozhige/'
    #books_url = 'http://www.sbkk88.com/mingzhu/gudaicn/sidamingzhu/'
    book_list = get_book_list(books_url)
    chapters = get_chapters(book_list)
    download(chapters)
