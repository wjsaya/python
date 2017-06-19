#coding: utf-8
#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
#Auther: wjsaya
from random import choice
import string
import os

def main():
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
        
def get_code(dict, length, count):
#根据给定字典，长度来得出激活码
    for i in range(0,int(count)):
        code = ""
    #通过count限制激活码个数，循环调用choice来计算激活码
        for i in range(0,int(length)):
            code = code+str(choice(dict))
        save_to_file(code)
    
def save_to_file(code):
#保存到文件
    with open ('activecode.code', 'a') as f:
        f.write(code+'\n')
     
def save_to_mysql(id, code):
    host = ("请输入数据库主机ip：")
    user = ("请输入数据库用户名：")
    pass = ("请输入数据库对应用户的密码：")
    db = ("请输入执行操作的数据库：")
    mysql = pymysql.connect(host, user, pass, db)
    cursor = mysql.cursor()
    sql = """ insert into `active` (`id`, `code`) VALUES
        (`id`, `code`);"""
    
    
if __name__ == "__main__":
    main()

