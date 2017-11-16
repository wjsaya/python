#!/usr/bin/env python3
#encoding:utf-8
#第一步：输入up主id，获取他的所有上传的信息。
import requests
import pymysql
import sth


def start_from_AV(AVnum):
    #拼接出up主的id，然后就能查询相关信息
    url_of_upinfo = ('https://api.bilibili.com/cardrich?mid=' + str(UPID))
    #加入av号，查询tag信息
    url_of_av_tags = ('https://api.bilibili.com/x/tag/archive/tags?aid=' + str(AVnum))
    #加入av好和up主id，查询给up充电的用户信息
    url_of_toubi = ('https://api.bilibili.com/x/web-interface/elec/show?aid=' + str(AVnum) + '&mid=' + str(UPID))
    #加入视频AV号，获取收藏等信息
    url_of_av_info = ('https://api.bilibili.com/x/web-interface/archive/stat?aid=' + str(AVnum))

def start_from_up(UPID):
    url = 'XXXXXX' + UPID
    html = requests.get(url, headers=sth.get_agent_pc()).text
    print (html)

    #拼接出up主的id，然后就能查询相关信息
    url_of_upinfo = ('https://api.bilibili.com/cardrich?mid=' + str(UPID))
    #加入av号，查询tag信息
    url_of_av_tags = ('https://api.bilibili.com/x/tag/archive/tags?aid=' + str(AVnum))
    #加入av好和up主id，查询给up充电的用户信息
    url_of_toubi = ('https://api.bilibili.com/x/web-interface/elec/show?aid=' + str(AVnum) + '&mid=' + str(UPID))
    #加入视频AV号，获取收藏等信息
    url_of_av_info = ('https://api.bilibili.com/x/web-interface/archive/stat?aid=' + str(AVnum))


if __name__ == '__main__':
    AV = 16341411
    start_url = ('https://www.bilibili.com/video/av'+str(AV))
    start_from_up(start_url)

