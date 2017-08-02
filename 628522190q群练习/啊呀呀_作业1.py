#!/usr/bin/env python3
import requests


#1.使用python抓取http://httpbin.org/get网页内容
def Fun1(url):

    print (requests.get(url).content.decode('utf-8'))

#2.还是抓取上面的内容，不过吧浏览器头（user-agent）更改为Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
def Fun2(url):

    head = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    print (requests.get(url, headers=head).content.decode('utf-8'))

#3. 使用python抓取http://httpbin.org/post网页内容（无论status_code为多少）
def Fun3(url):

    print (requests.get(url).content.decode('utf-8'))


#4.使用python向http://httpbin.org/post 提交{&#39;python&#39;:&#39;python&#39;},注意，这边请求方法为post
def Fun4(url):
        data4 = {'python':'python'}
        print (requests.post(url, data=data4).content.decode('utf-8'))

if __name__ == "__main__":
    Fun1('http://httpbin.org/get')
    Fun2('http://httpbin.org/get')
    Fun3('http://httpbin.org/post')
    Fun4('http://httpbin.org/post')