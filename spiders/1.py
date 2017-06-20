#coding: utf-8
import urllib
import http.cookiejar

url = "http://c.highpin.cn/Users/CLogin"
postdata =urllib.parse.urlencode({    
"Logon_Password":"sunmin",
"Logon_PostCode":"fghc",
"Logon_RememberMe":"false",
"Logon_UserEmail":"sun121@qq.com"
}).encode('utf-8')
header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"utf-8",
"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"Connection":"keep-alive",
"Host":"c.highpin.cn",
"Referer":"http://c.highpin.cn/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}
req = urllib.request.Request(url,postdata,header)
##print(urllib.request.urlopen(req).read().decode('utf-8'))

#自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)# 安装opener到全局
r = opener.open(req)
print(r.read().decode('utf-8'))
