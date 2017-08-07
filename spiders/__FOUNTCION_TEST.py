import requests
import sth
import re

#url = 'http://www.720ta.com/vod-detail-id-721.html'
#url = 'http://www.720ta.com/kan.php?from=flv&url=227152'
url = 'http://91kan2.720down.top/225286.mp4'



html = requests.get(url, stream=True, headers=head).content
#print (re.findall(R, html))
print (html)

