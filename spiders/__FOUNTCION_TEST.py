import requests
import re
base_url ="http://www.sbkk88.com"
q = '卷1：权力的游戏 Chapter1 序曲'
url = "/mingzhu/waiguowenxuemingzhu/bingyuhuozhige/b1/145664.html"


options = (r'(<p>.*</p>)')
html = requests.get(base_url+url).content.decode("gbk")
temp =  (re.findall(options, html))
print (temp)
for i in range(0,len(temp)):
    lines = temp[i]
    lines = lines.replace('<u>一</u>','')
    lines = lines.replace('<p>','')
    lines = lines.replace('</p>','\n')
    with open('./'+q, 'a') as f:
        f.write(lines)

