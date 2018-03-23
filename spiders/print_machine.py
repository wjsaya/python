#!/usr/bin/env python3
#!coding: utf-8

#http://yinka.co/library/preview?id=5461192
import time
import requests
from lxml import etree
from selenium import webdriver
import urllib.parse as UP
import logging

logging.basicConfig(
    filename='./yinba.log',
    format='[%(asctime)s][%(name)s][%(levelname)s][%(module)s]:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.INFO)

def get_url(file_ids):
    base = 'http://yinka.co/library/preview?id='
    for file_id in file_ids:
        time.sleep(5)
        logging.info('sleeping 5 seconds...')
        get_html (base + file_id)
    
   # get_html('http://yinka.co/library/preview?id=5461192')

def get_html(url):
    logging.info("开始解析"+url)
#    s = requests.Session()
#    html = s.get(url)
#    print (html.text)
    PJ = webdriver.PhantomJS()
#    PJ = webdriver.Chrome()
    PJ.get(url)
    html_so = etree.HTML(PJ.page_source.encode('utf-8'))
   # f = open('1.html', 'r',encoding="utf-8")
    #html = f.read()
    #print (html)
    #f.close()
    try:
        file_name = html_so.xpath("//span[@ng-bind='lib.filename']")[0].get('title')
    except Exception as e:
        logging.error(e)
    try:
        file_url1 = html_so.xpath("//iframe[@id='preview-content']")[0].get('ng-src')
    except Exception as e:
        logging.error(e)
    try:
        file_url = UP.unquote(file_url1).replace('./views/pdf/viewer.html?file=','')
    except Exception as e:
        logging.error(e)

    try:
        file_details = requests.get(file_url).content
        with open ('./pdf/'+file_name, 'wb') as f:
            f.write(file_details)
            logging.info(file_name+"已下载")
    

    except Exception as e:
        logging.error(e)
   

if __name__ == '__main__':
        with open ('file_id.txt','r') as f:
            get_url(f.readlines())


