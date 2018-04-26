#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wjsaya


import requests
import logging
import time
import pymysql
from prettytable import PrettyTable

logging.basicConfig(
    filename='./12306_query.log',
    format='[%(asctime)s][%(name)s][%(levelname)s][%(module)s]:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.INFO)

get_cookies = {
'_jc_save_fromDate':'2018-03-30',
'_jc_save_fromStation':'成都东,ICW',
'_jc_save_toDate':'2018-03-30',
'_jc_save_toStation':'广汉,GHW',
'_jc_save_wfdc_flag':'dc',
'BIGipServerotn':'1944584458.24610.0000',
'JSESSIONID':'A9B9F8A9A08F755105061E9AF0126CC6',
'RAIL_DEVICEID':'gKTdhbpjhdP6kDM9Lrv4nopxmkeAlPfRfbb_Nt7-P8ZMgoNrSFJ_3pGCljJDf4iBAKfhtUpES1adUYsrQ3X2RZBoC6dlITAbCjXsnqCGVe-AwVi9zDbj4-OqbX7SBlujKbGQyipa-7tOLd1UA3CbZe6vNWuoB78A',
'RAIL_EXPIRATION':'1521035583907',
'route':'c5c62a339e7744272a54643b3be5bf64'
}

get_head = {
'Host':'kyfw.12306.cn',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:59.0) Gecko/20100101 Firefox/59.0',
'Accept':'*/*',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding':'gzip, deflate, br',
'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
'If-Modified-Since':'0',
'Cache-Control':'no-cache',
'X-Requested-With':'XMLHttpRequest',
'DNT':'1',
'Connection':'keep-alive',
'Pragma':'no-cache'
}

post_head = get_head
post_head.update({'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate, br',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT':'1',
    'Pragma':'no-cache'
    })

def ticket_list(from_st, to_st, go_date):
    '''
    可指定时间，如果未指定，那就取当天
    '''
    if len(go_date) == 0:
        go_date = time.strftime('%Y-%m-%d', time.localtime())
    '''
    查询from_st到to_st的go_date的车票
    '''
    code, from_stc, to_stc = get_city_code(from_st, to_st)
    if code != 2:
        print ('获取站点对应的代码失败')
        exit()
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date='+go_date+'&leftTicketDTO.from_station='+from_stc+'&leftTicketDTO.to_station='+to_stc+'&purpose_codes=ADULT'
    try:
        rsp = requests.get(url, headers=get_head, cookies=get_cookies).json()
    except:
        logging.info('余票查询接口，解析返回json报文失败')
        return 1
    try:
        f2t = rsp['data']['map']
    except:
        print(rsp)
        logging.info("获取信息失败");
        return 1
    #logging.info ("查询内容"+"\t"+"车次"+"\t"+"出发"+"\t"+"到达"+"\t"+"历时"+"\t"+"一等"+"\t"+"二等"+"\t"+"无座")
    train_list = PrettyTable(["发车日期", "车次", "买_起", "买_终", "买_出发", "买_到达", "买_历时", "可网购", "特等座", "无座", "硬卧", "硬座", "二等", "一等", "商务座", "备注"])
    
    train_list.padding_width = 1
    train_list.align = 'l'

    conn = pymysql.connect(host='localhost', user='pylocal', password='123456', db='train', charset='utf8')
    cur = conn.cursor()
    for t in rsp['data']['result']:
        b = "".join(t)
        c = b.split('|')
        #logging.info (f2t[0]+"-->"+f2t[1]+"\t"+c[3]+"\t"+c[8]+"\t"+c[9]+"\t"+c[10]+"\t"+c[31]+"\t"+c[30]+"\t"+c[26])
        train_list.add_row([c[13], c[3], f2t[c[6]], f2t[c[7]], c[8], c[9], c[10], c[11], c[25], c[26], c[28], c[29], c[30], c[31], c[32], c[1]])
        sqli = 'insert into query(发车日期, 车次, 买_起, 买_终, 买_出发, 买_到达, 买_历时, 可网购, 特等座, 无座, 硬卧, 硬座, 二等, 一等, 商务座, 备注) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'
        cur.execute(sqli % (c[13], c[3], f2t[c[6]], f2t[c[7]], c[8], c[9], c[10], c[11], c[25], c[26], c[28], c[29], c[30], c[31], c[32], c[1]))
        conn.commit()
    
    cur.close()
    conn.close()


    logging.info('\n' + str(train_list))
    #logging.info('------------------------------------------------------------------------------------------------------')
    logging.info('-------------------------[query time]=[' +  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ']-----------------------')

def order_query():
    cookie = {
    'BIGipServerotn':'367264266.38945.0000',
    'BIGipServerpool_passport':'250413578.50215.0000',
    'JSESSIONID':'EC7AE826BA26B632D5CBC15411543299',
    'RAIL_DEVICEID':'dLVA5WOAR4wYoA8t_0w0B9Z-QXm36ORFmcfLk6Eggl6e2AMppc1JKaGvi5EmahFHG9XsHWSUlnIkkgbxIzsLbs9JC5TSWYxslfRgyYFFsyU_isJdo6Ql3YM4pjSWIsZr1F5wmos5_J_HHSlcFbsibavpbXEjk-aL',
    'RAIL_EXPIRATION':'1518318152117',
    'route':'9036359bb8a8a461c164a04f8f50b252',
    'tk':'hDGPDWNyhRMa3_eOswx-OYecPQ50ES4-5P1Dke02WpE09w2w0'
    }

    data = {
    'queryType':'1',
    'queryStartDate':'2018-02-01',
    'queryEndDate':'2018-02-07',
    'come_from_flag':'my_order',
    'pageSize':'8',
    'pageIndex':'0',
    'query_where':'G',
    'sequeue_train_name':''
    }

    q_url = 'https://kyfw.12306.cn/otn/queryOrder/queryMyOrder'
    a = requests.post(q_url, headers=post_head, cookies=cookie, data=data)
    print (a.content.decode('utf-8'))


def init_city():
    '''
    获取站点名与代号的对应关系js，分为3步
        1，从网站获取站点js文件
        2，保存源文件到本地
        3。解析源文件为站点文件station
        station文件大致结构：
         字段0 : 火车站名称汉语拼音首字母 字段1 : 火车站名称汉语 字段2 : 在查票的时候火车站的代码 (比如说 : 上海的代码即为 SHH) 字段3 : 火车站名称汉语拼音 字段4 : 火车站名称汉语拼音首字母 (模糊匹配 : 比如说输入 北京南站 , 那么有可能也有 北京站 的信息) 字段5 : 火车站编号(数字的序号 , 应该是铁道部或者网站自己定义的 , 应该是用于唯一标识某一个火车站)
    '''
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9047'
    rsp = requests.get(url, headers=get_head)
    with open ('./station_name.js', 'w') as f1:
        f1.write(rsp.content.decode('utf-8'))
    with open ('./station_name.js') as f2:
        line = f2.readlines()[0][21:-2]
        #21，前21个字符，即【var station_names ='@】bjb|北京北|VAP|beijingbei|bjb|0
        #去掉最后两个字符，即去掉【@zzn|株洲南|KVQ|zhuzhounan|zzn|2723';】后面的【';】
        Z = line.split("@")
        #用@分隔字符串，一个@后面是一个站点
    with open ('./station', 'w') as f3:
        for i in Z:
            f3.write(i + '\n')

def get_city_code(city_name1, city_name2):
    flag = 0
    with open ('/public/crontab/12306/station', 'r') as f2:
        for i in f2.readlines():
            line = i.split('|')
            if (line[1] == city_name1):
                flag += 1
                code1 = line[2]
            if (line[1] == city_name2):
                flag += 1
                code2 = line[2]
        if (flag == 2):
            print (flag, code1, code2)
            return (flag, code1, code2)
        else:
            return (flag, '', '')


def main():
    from_st='成都东'
    to_st='广汉'
    go_date='2018-03-30'
    time.sleep(2)
    ticket_list(from_st, to_st, go_date)
    time.sleep(5)
    ticket_list(from_st, to_st, go_date)
    time.sleep(8)
    ticket_list(from_st, to_st, go_date)
        
if __name__ == '__main__':
    #init_city()
    main()
    #order_query()

