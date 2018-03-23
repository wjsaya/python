#!/usr/bin/env python3
#encoding:utf-8
#第一步：输入up主id，获取他的所有上传的信息。
import requests
import time
import sth
import pymysql
import user_analyse
import video_analyse

def get_upid_fromwaiting(u_sql, p_sql, default):
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, charset='utf8', db='bilibili')
    cur = conn.cursor()
    try:
        cur.execute('select mid from up_waiting order by no limit 1;')
        UPID = cur.fetchone()[0]
        mid_del = ('delete from up_waiting where mid='+str(UPID))
        print ('已从数据库获取到UPID='+str(UPID)+'此数据已经从up_waiting表中删除')
        cur.execute(mid_del)
        cur.close()
        conn.commit()
        conn.close()
    except Exception as e:
        UPID = default
        print (e)
    return UPID

def get_up_info(url):
    try:
        json = requests.get(url).json()['data']['card']
        user_analyse.insert_into_up_info(u_sql, p_sql, json) 
    except Exception as e:
        print (e)

def get_upid_fromdb(u_sql, p_sql):
    mid = 1
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, charset='utf8', db='bilibili')
    cur = conn.cursor()
    cur.execute('select mid from up_info order by mid limit 1;')
    for i in cur.fetchall():
        print (i[0])
    return mid

def get_av_of_up(url):
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, charset='utf8', db='bilibili')
    



if __name__ == '__main__':
    while (True):
        AV = 16341411
        u_sql = 'pylocal'
        p_sql = '123456'
        user_analyse.db_init(u_sql, p_sql)
        #UPID = get_upid_fromwaiting(u_sql, p_sql, default='592761')
        #print ("开始抓取"+str(UPID)+"的账户信息")
        #url_of_upinfo = ('https://api.bilibili.com/cardrich?mid=' + str(UPID))
        #get_up_info(url_of_upinfo)

        UPID = get_upid_fromdb(u_sql, p_sql)
        url_of_up_space = ('https://space.bilibili.com/' + str(UPID))
        get_av_of_up(url_of_up_space)
        break