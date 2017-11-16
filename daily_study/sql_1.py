#!/usr/bin/env python3
#!coding: utf-8

import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='pyroot',password='123456qwe')

conn.query("drop database test")
conn.query("create database test")
conn.query("use test")
conn.query("create table t(row1 int,row2 int,row3 varchar(10))")
conn.commit()

cur=conn.cursor()
for row1 in range(0,9):
    for row2 in range(0,9):
        for row3 in range(0,9):
            cur.execute("insert into t values(row1,row2,row3)")

cur.execute("select * from t")
cur.close()
conn.commit()
conn.close()        



