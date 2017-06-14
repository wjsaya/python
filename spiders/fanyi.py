#coding: utf-8
import requests
import json

def translate(word=None):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key={
    'type':"AUTO",
    'i':word,
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_CLICKBUTTON",
    "typoResult":"true"
    }
    response = requests.post(url,data=key)
    result = json.loads(response.text)
    return result

def get_result(li=None):
    print ("输入的词为：%s" % li['translateResult'][0][0]['src'])
    print ("翻译结果为：%s" % li['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    print ("本程序调用有道词典的API进行翻译，可达到以下效果：")
    print ("外文-->中文")
    print ("中文-->英文")
    word = input('请输入你想要翻译的词或句：')
    list_trans = translate(word)
    get=get_result(list_trans)

    
