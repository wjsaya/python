#!/usr/bin/env python3
#encoding:utf-8
import pymysql
import time

def db_init(u_sql, p_sql):
    conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql)
    conn.query('create database if not exists bilibili')
    conn.query('use bilibili')
    conn.query('create table if not exists up_info (mid varchar(20),name varchar(200),sex varchar(20),regtime int,birthday varchar(200),place varchar(20),description varchar(200),fans int,attention int,sign varchar(200),level int,vipStatus int,article int,nameplant_name varchar(200),nameplant_level varchar(200),nameplant_condition varchar(200),official_type int,official_verify varchar(200));')
    conn.query('create table  if not exists up_relation (mid int, attentions int);')
    conn.close()

def insert_into_up_info(u_sql, p_sql, json):
    mid = json['data']['card']['mid']
    name = json['data']['card']['name']
    sex = json['data']['card']['sex']
    regtime = json['data']['card']['regtime']
    birthday = json['data']['card']['birthday']
    place = json['data']['card']['place']
    description = json['data']['card']['description']
    fans = json['data']['card']['fans']
    attention = json['data']['card']['attention']
    sign = json['data']['card']['sign']
    level_info_current_level = json['data']['card']['level_info']['current_level']
    vipStatus = json['data']['card']['vip']['vipStatus']
    article = json['data']['card']['article']
    nameplate_name = json['data']['card']['nameplate']['name']
    nameplate_level = json['data']['card']['nameplate']['level']
    condition = json['data']['card']['nameplate']['condition']
    official_verify_type = json['data']['card']['official_verify']['type']
    official_verify_desc = json['data']['card']['official_verify']['desc']
    print("%s"+str(type(mid)))
    print("%s"+str(type(name)))
    print("%s"+str(type(sex)))
    print("%d"+str(type(regtime)))
    print("%s"+str(type(birthday)))
    print("%s"+str(type(place)))
    print("%s"+str(type(description)))
    print("%d"+str(type(fans)))
    print("%d"+str(type(attention)))
    print("%s"+str(type(sign)))
    print("%d"+str(type(level_info_current_level)))
    print("%d"+str(type(nameplate_name)))
    print("%d"+str(type(nameplate_level)))
    print("%s"+str(type(vipStatus)))
    print("%s"+str(type(article)))
    print("%s"+str(type(condition)))
    print("%d"+str(type(official_verify_type)))
    print("%s"+str(type(official_verify_desc)))
#其中四条顺序反了，nameplant_name附近


    conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql, db='bilibili')
    row = conn.cursor()
    sql_update ="insert into up_info values(%s,%s,%s,%d,%s,%s,%s,%d,%d,%s,%d,%d,%d,%s,%s,%s,%d,%s)"
    row.execute(sql_update % (mid,name,sex,regtime,birthday,place,description,fans,attention,sign,level_info_current_level,nameplate_name,nameplate_level,vipStatus,article,condition,official_verify_type,official_verify_desc))

    row.close()
    conn.commit()
    conn.close()
    
