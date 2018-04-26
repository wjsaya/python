#!/usr/bin/env python3
#encoding:utf-8
import pymysql
import time

def db_init(u_sql, p_sql):
    conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql, charset="utf8")
    conn.query('create database if not exists bilibili')
    conn.query('use bilibili')
    conn.query('create table if not exists up_info (mid int NOT NULL PRIMARY KEY,name varchar(200),sex varchar(20),regtime int,birthday varchar(200),place varchar(20),description varchar(200),fans int,attention int,sign varchar(200),level int,vipStatus int,article int,nameplant_name varchar(200),nameplant_level varchar(200),nameplant_condition varchar(200),official_type int,official_verify varchar(200));')
    conn.query('create table  if not exists up_relation (mid int, attention int);')
    conn.query('create table  if not exists up_waiting (no int AUTO_INCREMENT PRIMARY KEY , mid int NOT NULL);')
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
    insert_into_up_info ="insert into up_info values(%s,%s,%s,%d,%s,%s,%s,%d,%d,%s,%d,%d,%d,%s,%s,%s,%d,%s);"
    insert_into_relation = "insert into up_relation values(%d,%d);"
    insert_into_waiting  = "insert into up_waiting values(%d,%d);"
    get_info_from_up_info = "select * from up_info where mid = %d;"
 
    try:
        row.execute(insert_into_up_info % (mid,name,sex,regtime,birthday,place,description,fans,attention,sign,level_info_current_level,vipStatus,article,nameplate_name,nameplate_level,nameplant_condition,official_verify_type,official_verify_desc))
    except Exception as e:
        print ("此up主已抓取？报错如下：")
        print (e)
    for i in r_list:
        try:
            row.execute(insert_into_relation % (int(mid),int(i)))
        except Exception as e:
            print ("此对应关系已记录？报错如下：")
            print (e)
        try:
            row.execute(get_info_from_up_info % int(i))
            print ("id为%d的用户已抓取，不用再次入库" % int(i))
        except Exception as e:
            row.execute(insert_into_waiting % (int(), int(i)))
            print ("UPID=%d已加入waiting库，待抓取" % int(i))
            print (e)
     
    row.close()
    conn.commit()
    conn.close()
