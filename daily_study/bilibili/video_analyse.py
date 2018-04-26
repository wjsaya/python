#!/usr/bin/env python3
#encoding:utf-8
import pymysql
import requests

def db_init(u_sql, p_sql):
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, db='bilibili', charset="utf8")
    conn.query('create table if not exists up_to_av (aid int NOT NULL PRIMARY KEY, mid int NOT NULL);')
    conn.query('create table  if not exists av_info (aid int NOT NULL PRIMARY KEY, view int, danmaku int, favorite int, coin int, share int, history_rank int, CONSTRAINT MID_NOT UNIQUE (aid, mid));')
    #history_rank = his_rank,历史最高全站日排行
    conn.close()

def get_page_num(url):
    html = requests.get(url).json()
    print (html)


if __name__ == '__main__':
    u_sql = 'pylocal'
    p_sql = '123456'
    UPID = 42697
   # db_init(u_sql, p_sql)
    url = ('https://space.bilibili.com/42697')
    url1 = 'https://api.bilibili.com/x/space/navnum?mid=883968&jsonp=jsonp'
    get_page_num(url1)




