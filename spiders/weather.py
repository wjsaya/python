#coding: utf-8
#获取成都未来15天的天气
import re
import requests
from bs4 import BeautifulSoup

url = 'http://chengdu.tianqi.com/15/'
def get_html(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content.decode("gbk"), "lxml")
    return soup

def get_weather(url):
    html = get_html(url)
    text = html.get_text()
    date = re.findall(r'..月..日', text)
    temp = re.findall(r'.*℃~.*', text)
    wea_day = re.findall(r'.*白天.*', text)
    wea_nig =re.findall(r'.*夜间.*', text)
   
    for i in range(0,len(date)):
        print ("日期："+str(date[i]))
        print ("温度："+str(temp[i]))
        print (str(wea_day[i]))
        print (str(wea_nig[i]))
        print ("##########################")

get_weather(url)
