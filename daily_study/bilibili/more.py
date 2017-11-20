#!/use/bin/env python3
#encoding: utf-8

from multiprocessing import Pool
import time
import multiprocessing
import pymysql
def insert_waiting(u_sql, p_sql, mid, i):
    print ("%s进程已启动,开始处理mid为%s的用户" % (multiprocessing.current_process().name, i))
    time.sleep(1)
    conn = pymysql.connect(host='localhost',port=3306,user=u_sql,password=p_sql, db='bilibili', charset="utf8")
    row = conn.cursor()
    insert_into_relation = "insert into up_relation values(%d,%d);"
    insert_into_waiting  = "insert into up_waiting values(%d,%d);"
    get_info_from_up_info = "select * from up_info where mid = %d;"
    try:
        row.execute(insert_into_relation % (int(mid),i))
    except Exception as e:
        print ("此对应关系已记录？报错如下：")
        print (e)
    conn.commit()
    try:
        print (row.execute(get_info_from_up_info % i))
        print ("id为%d的用户已抓取，不用再次入库" % i)
    except Exception as e:
        row.execute(insert_into_waiting % (int(), i))
        print ("UPID=%d已加入waiting库，待抓取" % i)
        conn.commit()
    row.close()
    conn.close()

if __name__ == '__main__':
    
    u_sql = 'pylocal'
    p_sql = '123456'
    mid = 592761
    flowing = Pool(2)
    for i in range(1,6):
        flowing.apply_async(func=insert_waiting, args=(u_sql, p_sql, mid, i,))

    print ('main ended')
    flowing.close()
    flowing.join()

