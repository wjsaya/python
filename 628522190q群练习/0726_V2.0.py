#/usr/bin/env python3
# coding: utf-8
# version: v2.0
'''
Date:2017-07-26
题型类型：Python爬虫练习
题目要求： 爬取小说《冰与火之歌》的1-5季内容并保存到本地。 （保存完别删，周六的时候会用到）
'''
import os
import re
from multiprocessing import Pool
from multiprocessing import current_process
import time
import requests
import sth


class Fenxi(object):
#nothing
    def __init__(self, url):
        self.__url = url

#    def tu(self):
#        self.tu_url_R = (r'^.*img src="(.*)" alt.*')
#        self.tu_name_R = (r'.*alt="(.*)"[/ ]*/>.*')
#        print (base_url+re.findall(self.tu_url_R, self.__url)[0])
#        print (re.findall(self.tu_name_R, self.__url)[0])

    def get_name_url(self):
        self.each_url_R = (r'.*href="(.*)" class="text".*')
        self.each_name_R = (r'.*"_blank" >(.*)</a> </li>')
        each_url = base_url + re.findall(self.each_url_R, self.__url)[0]
        each_url_name = re.findall(self.each_name_R, self.__url)[0]
        return (each_url_name, each_url)

    def get_page_url(self):
        # 传入单本书的页面url
        name_list = []
        url_list = []
        html = requests.get(
            self.__url, headers=sth.get_agent_pc()).content.decode("gbk")
        self.each_name_R = (r' <li> <a href=(.*).*</a> </li>')
        each_url_name = re.findall(self.each_name_R, html)
        each_url_name = each_url_name[0].replace('<li> <a href=', '\r\n')
        each_url_name = each_url_name.replace(
            ' class="articleTitle"  target="_blank">', '')
        each_url_name = each_url_name.replace('</a> </li>', '')
        each_url_names = each_url_name.split('"')
# 一大串replace是为了转换地址,从下方的URL1转化为URL2，最终通过给定的分隔符"来切割字段，形成一个列表。

# URL1：<li> <a href="/mingzhu/gudaicn/shuihuchuan/41951.html" class="articleTitle"  target="_blank">读后感——江湖好汉为何爱吃酱牛肉、不喜红烧肉之小考'
# URL2："/mingzhu/gudaicn/shuihuchuan/41951.html"读后感——江湖好汉为何爱吃酱牛肉、不喜红烧肉之小考
        for i in range(1, len(each_url_names)):
            # 循环列表，列表中的偶数位字段则为名字，奇数位字段的为url。取出之后放入两个列表。
            if (i % 2) == 0:
                name_list.append(each_url_names[i])
            else:
                url_list.append(each_url_names[i])

        Multi = Pool(4)
        for i in range(0, len(name_list)):
            file_name = re.sub(r"[/\\:*?\"<>|]+", '',name_list[i])
            Multi.apply(self.download, args=(file_name, url_list[i],))
# 因为网站那边肯定有反爬机制，因此设定爬取五个页面就暂停1.5秒再继续，同时headers里的user-agent是随机抽取的，因此隐蔽性略微提高。
# 调用download，提取网页上的问题并以给定的文件名保存到本地
        Multi.close()
        Multi.join()

    def download(self, name, url):
        print("开始下载%s" % name)
        base_url = "http://www.sbkk88.com"
        file_name = name
        if os.path.exists("./" + file_name):
            print(file_name + "已下载，跳过")
        else:
            url = url
            options = (r'(<p>.*</p>)')
            options2 = (r'(.*</p>)<p>')
            options3 = (r'(.+)<br>')
            options4 = (r'(<br>)')
            html = requests.get(
                base_url + url, headers=sth.get_agent_pc()).content.decode("gbk")
            temp = (re.findall(options, html))
            #print (file_name+":"+base_url+url)

    # option
    #<p>“渔家女孩告诉我，他们中下阶层的百姓有个更妙的比喻：国王吃席，首相”</p>

    # options2
    # 诸般买卖无商旅，各样生涯不见人。殿上君王归内院，阶前文武转衙门。</p><p>

    # options3
    #　　一局输赢料不真，香销茶尽尚逡巡。<br>

    # options4
    #<br>

            if temp == []:
                # 特别恶心人的一点，网站里面的正文有两种格式甚多种，目前找到两种，但是爬取时又有没有抓到的页面，此部分待完善。
                # 而且网站还在网页中间插入了<u>一</u>这种东西，不知道还有没有插入其他的东西，但是真的好恶心。。。
                temp = (re.findall(options2, html))

            for i in range(0, len(temp)):
                # 循环遍历每一行，去除特殊字符并且用</p>来换行。
                lines = temp[i]
                lines = lines.replace('<u>一</u>', '')
                lines = lines.replace('<p>', '')
                lines = lines.replace('</p>', '\n')
                file_name = file_name.replace('\r\n', '')

                with open('./' + file_name, 'a') as f:
                    f.write(lines)

    #<a href="/mingzhu/waiguowenxuemingzhu/bingyuhuozhige/b1/145664.html" class="articleTitle" target="_blank">卷1：权力的游戏 Chapter1 序曲</a>


def get_books_list(book_url):
    # 返回列表，为当前页下包含小说的li标签
    html = requests.get(book_url, headers=sth.get_agent_pc()).content.decode('gbk')
    options = (r'<li>.*class="ablum".*</li>')
    each_book_list = re.findall(options, html)
    name_list1 = []
    url_list = []
    #print (each_book_list)
    for url in each_book_list:
        TEMP_chapter = Fenxi(url)
        # 初始化TEMP_chapter对象，然后通过调用类里面的get_name_url方法来获取每本书的名字和链接，然后分别追加到各自列表
        name_list1.append(TEMP_chapter.get_name_url()[0])
        url_list.append(TEMP_chapter.get_name_url()[1])
    return (name_list1, url_list)


def download(books_list):
    # 传入两个列表，一个为分部的名字，一个为分部的链接，然后创建文件夹和文件，最终调用类里面的get_page_url方法来获取书本里的每章。
    names = books_list[0]
    urls = books_list[1]
    for count in range(0, len(names)):
        sth.change_dir('./小说下载')
        sth.change_dir(names[count])
        chapter = Fenxi(urls[count])
        #if names[count] == "冰与火之歌5":
        chapter.get_page_url()
        sth.change_dir('../../')


if __name__ == '__main__':
    base_url = "http://www.sbkk88.com"
    #books_url = 'http://www.sbkk88.com/mingzhu/waiguowenxuemingzhu/bingyuhuozhige/'
    books_url = 'http://www.sbkk88.com/mingzhu/gudaicn/sidamingzhu/'
    #udge = input("下载地址是的是合辑页？还是单本页？")
    print(books_url)
    books_list = get_books_list(books_url)
    # books_list为解析出的书本合辑中每本书的名字和url列表，内部包含XXX第一部，XXX第二部，XXX第三部这种。
    download(books_list)
    # 调用下载
