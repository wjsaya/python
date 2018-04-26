
def start_from_AV(AVnum):
    #拼接出up主的id，然后就能查询相关信息
    url_of_upinfo = ('https://api.bilibili.com/cardrich?mid=' + str(UPID))
    #加入av号，查询tag信息
    url_of_av_tags = ('https://api.bilibili.com/x/tag/archive/tags?aid=' + str(AVnum))
    #加入av号和up主id，查询给up充电的用户信息
    url_of_toubi = ('https://api.bilibili.com/x/web-interface/elec/show?aid=' + str(AVnum) + '&mid=' + str(UPID))
    #加入视频AV号，获取收藏等信息
    url_of_av_info = ('https://api.bilibili.com/x/web-interface/archive/stat?aid=' + str(AVnum))

def get_html(url):
    html = requests.get(url, headers=sth.get_agent_pc()).text
    print (html)


def start_from_up(UPID):
    start_url = ('https://www.bilibili.com/space/'+str(UPID))
    html = requests.get(start_url, headers=sth.get_agent_pc()).text
    print (html)
    #拼接出up主的id，然后就能查询相关信息
    url_of_upinfo = ('https://api.bilibili.com/cardrich?mid=' + str(UPID))
    #加入av号，查询tag信息
    url_of_av_tags = ('https://api.bilibili.com/x/tag/archive/tags?aid=' + str(AVnum))
    #加入av好和up主id，查询给up充电的用户信息
    url_of_toubi = ('https://api.bilibili.com/x/web-interface/elec/show?aid=' + str(AVnum) + '&mid=' + str(UPID))
    #加入视频AV号，获取收藏等信息
    url_of_av_info = ('https://api.bilibili.com/x/web-interface/archive/stat?aid=' + str(AVnum))
