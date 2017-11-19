#!/usr/bin/env python3
#encoding:utf-8
#第一步：输入up主id，获取他的所有上传的信息。
import requests
import time
import sth
import pymysql
import sqlconn

def get_up_info(url):
    json = requests.get(url).json()['data']['card']
    sqlconn.insert_into_up_info(u_sql, p_sql, json) 

def get_upid(u_sql, p_sql, default):
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, charset='utf8', db='bilibili')
    cur = conn.cursor()
    try:
        cur.execute('select mid from up_waiting order by no limit 1;')
        UPID = cur.fetchone()[0]
        mid_del = 'delete from up_waiting where mid='+str(UPID)
        print (mid_del)
        cur.execute(mid_del)
        cur.close()
        conn.commit()
        conn.close()
    except Exception as e:
        UPID = default
        print (e)
    return UPID


if __name__ == '__main__':
    while (True):
        AV = 16341411
        u_sql = 'pylocal'
        p_sql = '123456'
        sqlconn.db_init(u_sql, p_sql)
        UPID = get_upid(u_sql, p_sql, default='592761')
        print ("开始抓取"+str(UPID))
        url_of_upinfo = ('https://api.bilibili.com/cardrich?mid=' + str(UPID))
        start_url = ('https://www.bilibili.com/video/av'+str(AV))
        get_up_info(url_of_upinfo)

