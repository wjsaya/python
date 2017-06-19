#coding: utf-8
#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
#Auther: wjsaya
from random import choice
import string
import os
import pymysql.cursors
       
def get_code(dict, length, count):
#根据给定字典，长度来得出激活码
    for i in range(1,int(count)+1):
        code = ""
    #通过count限制激活码个数，循环调用choice来计算激活码
        for l in range(0,int(length)):
            code = code+str(choice(dict))
        save_to_mysql(i, code)
    
def save_to_file(code):
#保存到文件
    with open ('activecode.code', 'a') as f:
        f.write(code+'\n')
     
def save_to_mysql(id, code):
#保存到mysql数据库
    host = ("192.168.122.18")
    user = ("root")
    pass_ = ("你的数据库密码")
    db = ("active")
    #设置数据库连接相关信息
    connect = pymysql.connect(host, user, pass_, db)
    cursor = connect.cursor()
    #链接数据库并设置游标
    sql = "insert into activeCode(id, code) VALUES ('%d', '%s')"
    data = (id, code)
    cursor.execute(sql % data)
    #执行sql语句
    
if __name__ == "__main__":
    if os.path.exists("./activecode.code"):
        print ("已经存在activecode.code文件，已经删除")
        os.remove("./activecode.code")
    dict = string.ascii_letters[:]
    #设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"
    get_code(dict, length, count)
