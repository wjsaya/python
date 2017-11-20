#!/usr/bin/env python3
#encoding:utf-8
import pymysql
import requests

def dba_init(u_sql, p_sql):
    conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql, charset="utf8")
    conn.query('create database if not exists bilibili')
    conn.query('use bilibili')
    conn.query('create table if not exists up_to_av (aid int NOT NULL PRIMARY KEY, mid int NOT NULL);')
    conn.query('create table  if not exists av_info (aid int NOT NULL PRIMARY KEY, view int, danmaku int, favorite int, coin int, share int, history_rank int, CONSTRAINT MID_NOT UNIQUE (aid, mid));')
    #history_rank = his_rank,历史最高全站日排行
    conn.close()


def db_init(u_sql, p_sql):
    pass