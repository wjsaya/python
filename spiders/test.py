# -*- coding: utf-8 -*-
import os
import re
import  requests
from bs4 import BeautifulSoup
import urllib

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3053.3 Safari/537.36'
}

session = requests.session()

def get(): #获取post表单中的两个数据  captcha-solutin   captcha-id
    url = 'https://www.douban.com/accounts/login?source=main'
    r1 = session.get(url,headers = header).text
    bs1 = BeautifulSoup(r1, 'lxml')
    solution = bs1.find('input', attrs={'name': 'captcha-id'}).get('value') #post表单内容中的captcha-solution参数的值
    imgurl = bs1.find('img', id="captcha_image").get('src') #验证码图片地址
    urllib.request.urlretrieve(imgurl, os.getcwd()+'\\11.jpg')  #下载验证码图片
    return solution

def log(zhanghao,mima,solution,id):
    loginurl = 'https://accounts.douban.com/login'
    data = {'source': "main",
           'redir': 'https://www.douban.com/note/629510365/',
           'form_email':zhanghao,
           'form_password':mima,
            'captcha-solution': solution,
            'captcha-id': id,
           'login':'登录'
    }
    content = session.post(loginurl,data=data,headers = header)
    print(content.text)

zhanghao = 'xxxx'
mima = 'xxx'
solution = get()
id = input("enter the id:") #根据下载的图片输入验证码
log(zhanghao,mima,solution,id)
