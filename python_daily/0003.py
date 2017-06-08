#coding: utf-8
#**第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
#Auther: wjsaya
from random import choice
import string
import redis
       
def get_code(dict, length, count):
#根据给定字典，长度来得出激活码
    for i in range(1,int(count)+1):
        code = ""
    #通过count限制激活码个数，循环调用choice来计算激活码
        for l in range(0,int(length)):
            code = code+str(choice(dict))
        save_to_redis(count, code)

def save_to_redis(max, value):
    #保存到redis数据库
    redisdb = redis.Redis(host='10.2.2.131',port=6379,db=0)
    redisdb.lpush('active_code',value)
    redisdb.lrange('active_code',0,max)
    redisdb.save()

    
if __name__ == "__main__":
    dict = string.ascii_letters[:]
    #设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"
    get_code(dict, length, count)
