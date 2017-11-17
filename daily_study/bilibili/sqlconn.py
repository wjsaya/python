#!/usr/bin/env python3
#encoding:utf-8

import pymysql

u_sql = 'pylocal'
p_sql = '123456'

conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql)
try:
    conn.query('use bilibili')
except Exception as e:
    conn.query('create database bilibili')
    sqlcommand = 'create table (
    conn.query('create table
