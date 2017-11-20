#!/usr/bin/env python3
#encoding:utf-8
import pymysql
import time
from multiprocessing import Pool
import multiprocessing
import requests

def db_init(u_sql, p_sql):
    conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql, charset="utf8")
    conn.query('create database if not exists bilibili')
    conn.query('use bilibili')
    conn.query('create table if not exists up_info (mid int NOT NULL PRIMARY KEY,name varchar(200),sex varchar(20),regtime int,birthday varchar(200),place varchar(20),description varchar(200),fans int,attention int,sign varchar(200),level int,vipStatus int,article int,nameplant_name varchar(200),nameplant_level varchar(200),nameplant_condition varchar(200),official_type int,official_verify varchar(200));')
    conn.query('create table  if not exists up_relation (mid int, attention int);')
    conn.query('create table  if not exists up_waiting (no int AUTO_INCREMENT PRIMARY KEY , mid int NOT NULL, CONSTRAINT MID_NOT UNIQUE (mid));')
    conn.close()

def insert_into_up_info(u_sql, p_sql, data):
    mid = data['mid']
    name = "'"+data['name']+"'"
    sex = "'"+data['sex']+"'"
    regtime = data['regtime']
    birthday = "'"+data['birthday']+"'"
    place = "'"+data['place']+"'"
    description = "'"+data['description']+"'"
    fans = data['fans']
    attention = data['attention']
    sign = "'"+data['sign']+"'"
    level_info_current_level = data['level_info']['current_level']
    vipStatus = data['vip']['vipStatus']
    article = data['article']
    nameplate_name = "'"+data['nameplate']['name']+"'"
    nameplate_level = "'"+data['nameplate']['level']+"'"
    nameplant_condition = "'"+data['nameplate']['condition']+"'"
    official_verify_type = data['official_verify']['type']
    official_verify_desc = "'"+data['official_verify']['desc']+"'"
    r_list = data['attentions']
    conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql, db='bilibili', charset="utf8")
    row = conn.cursor()
    insert_into_up_info1 ="insert into up_info values(%s,%s,%s,%d,%s,%s,%s,%d,%d,%s,%d,%d,%d,%s,%s,%s,%d,%s);" 
    try:
        row.execute(insert_into_up_info1 % (mid,name,sex,regtime,birthday,place,description,fans,attention,sign,level_info_current_level,vipStatus,article,nameplate_name,nameplate_level,nameplant_condition,official_verify_type,official_verify_desc))
    except Exception as e:
        print (e)
    row.close()
    conn.commit()
    conn.close()

    flowing = Pool(5)
    for i in r_list:
        flowing.apply_async(func=insert_waiting, args=(u_sql, p_sql, mid, i, ))
    print ("%s关注的up主开始对比" % mid)
    flowing.close()
    flowing.join()




def insert_waiting(u_sql, p_sql, mid, i):
    print ("%s进程已启动,开始处理mid为%s的用户" % (multiprocessing.current_process().name, i))
    #time.sleep(1)
    conn = pymysql.connect(host='localhost', port=3306, user=u_sql, password=p_sql, db='bilibili', charset="utf8")
    row = conn.cursor()
    insert_into_relation = "insert into up_relation values(%d,%d);"
    insert_into_waiting  = "insert into up_waiting values(%d,%d);"
    get_info_from_up_info = "select * from up_info where mid = %d;"
    try:
        row.execute(insert_into_relation % (int(mid),i))
    except Exception as e:
        print (e)
    conn.commit()
    if ( row.execute(get_info_from_up_info % i) == 1 ):
        print ("id为%d的用户已抓取，不用再次入库" % i)
    else:
    #except Exception as e:
        row.execute(insert_into_waiting % (int(), i))
        print ("UPID=%d已加入waiting库，待抓取" % i)
        conn.commit()
    row.close()
    conn.close()
    return 0

if __name__ == '__main__':
    u_sql = 'pylocal'
    p_sql = '123456'
    UPID = '592761'
    time.sleep(1)
    url = ('https://api.bilibili.com/cardrich?mid=' + UPID)
    json = requests.get(url).json()['data']['card']
    db_init(u_sql, p_sql)
    insert_into_up_info(u_sql, p_sql, json)