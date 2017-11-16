import urllib
  
HEADERS = {"cookie": ''}#里面写你在www.douban.com的cookie  
url = 'http://www.douban.com/'  
req = urllib2.Request(url, headers=HEADERS)  
text = urllib2.urlopen(req).read()  
  
if "首页设置".decode("gbk").encode("utf8") in text and "说句话".decode("gbk").encode("utf8") in text:  
    print ("登陆成功!" )
else:  
    print ("登录失败!"  )