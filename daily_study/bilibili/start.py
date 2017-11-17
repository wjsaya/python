#!/usr/bin/env python3
#encoding:utf-8
#第一步：输入up主id，获取他的所有上传的信息。
import requests
import sth
import sqlconn


def get_up_info(url):
    json = requests.get(url, headers=sth.get_agent_pc()).json()
    sqlconn.insert_into_up_info(u_sql, p_sql, json)
    #for i in json['data']['card']['attentions']:
    #    print (i)
    print(type( json['data']['card']['mid']))
    print(type( json['data']['card']['name']))
    print(type( json['data']['card']['sex']))
    print(type( json['data']['card']['regtime']))
    print(type( json['data']['card']['birthday']))
    print(type( json['data']['card']['place']))
    print(type( json['data']['card']['description']))
    print(type( json['data']['card']['fans']))
    print(type( json['data']['card']['attention']))
    print(type( json['data']['card']['sign']))
    print(type( json['data']['card']['level_info']['current_level']))
    print(type( json['data']['card']['vip']['vipStatus']))
    print(type( json['data']['card']['article']))
    print(type( json['data']['card']['nameplate']['name']))
    print(type( json['data']['card']['nameplate']['level']))
    print(type( json['data']['card']['nameplate']['condition']))
    print(type( json['data']['card']['official_verify']['type']))
    print(type( json['data']['card']['official_verify']['desc']))

if __name__ == '__main__':
    UPID=592761
    AV = 16341411
    u_sql = 'pylocal'
    p_sql = '123456'
    sqlconn.db_init(u_sql, p_sql)
    print ('数据库初始化完毕')
    url_of_upinfo = ('https://api.bilibili.com/cardrich?mid=' + str(UPID))
    start_url = ('https://www.bilibili.com/video/av'+str(AV))
    #start_from_up(16539048)
    get_up_info(url_of_upinfo)

