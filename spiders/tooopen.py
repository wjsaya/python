#coding: utf-8
import requests
from bs4 import BeautifulSoup
import os



def download_img(url,name):
#此函数通过获取到的图片链接来现在图片并根据网页标题命名
    img=requests.get(url)
    with open('./'+floder+'/'+name+'.jpg','wb') as file:
        file.write(img.content)
    print (name+" is downloaded")



def get_img_url(url):
#此函数获取详情页面中的图片链接
    j = requests.get(url)
    jj = BeautifulSoup(j.text,"lxml")
    jjj = jj.find_all(id="imgView")
    for i in jjj:
        download_img(i.get('src'),i.get('alt'))

def get_url(url):
#此函数从首页获取首页图片对应的详情链接
    r = requests.get(url)
    rr = BeautifulSoup(r.text,"lxml")
    rrr = rr.find_all(class_="pic")
    for i in  rrr:
        get_img_url(i.get('href'))


url=input("请输入素材公社（http://www.tooopen.com）中你想要下载的分类的url地址:")
num=input("请输入想获取的页数：")
floder=url[27:33]
os.mkdir(floder)
for i in range(1,int(num)+1):
    k=url[0:33]+"_1_"+str(i)+".aspx"
    get_url(k)
