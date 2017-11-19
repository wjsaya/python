#!/usr/bin/env python3
#encoding:utf-8
import pymysql
import time
u_sql = 'pylocal'
p_sql = '123456'

conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql, db='bilibili', charset="utf8")
row = conn.cursor()
get_info_from_up_info = "select count(mid) from up_info;"
for i in (row.execute(get_info_from_up_info))
    print(i)
row.close()
conn.commit()
conn.close()
