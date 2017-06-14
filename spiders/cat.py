#coding: utf-8
import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/700/700')
cat_img = response.read()

with open ('cat_700_700.jpg', 'wb') as cat:
    cat.write(cat_img)
