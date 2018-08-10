#!/usr/bin/env python3
#!coding: utf-8

import pymysql
import time
import multiprocessing

def get_mid(u_sql, p_sql):
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, db='bilibili', charset="utf8")
    cur = conn.cursor()
    s = 'select mid from up_info order by mid;'
    cur.execute(s)
    select = cur.fetchall()[0][0]
    print (select)


def form_date(u_sql, p_sql, mid):
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, db='bilibili', charset="utf8")
    cur = conn.cursor()
    select = 'select regtime from up_info where mid = %d;'
    cur.execute(select % mid)
    for i in cur.fetchall():
        print (i[0])
    cur.close()
    conn.commit()
    conn.close()

    #var e = new Date(1e3 * t)
    #return e.getFullYear() + "-" + (e.getMonth() + 1) + "-" + e.getDate()
   
if __name__ == '__main__':
    config = {
          'host':'127.0.0.1',
          'port':3306,#MySQL默认端口
          'user':'pylocal',#mysql默认用户名
          'password':'123456',
          'db':'bilibili',#数据库
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
          }
    u_sql = 'pylocal'
    p_sql = '123456'
    get_mid(u_sql, p_sql)