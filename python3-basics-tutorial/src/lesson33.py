'''
Created on Jan 29, 2017

@author: ubuntu
'''
import urllib.request
import re

url = 'http://pythonprogramming.net'
values = {'s':'basic','submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
res = urllib.request.urlopen(req)

resData = res.read()

parags = re.findall(r'<p>(.*?)</p>', str(resData))

for parag in parags:
    print('==================')
    print(parag)
    print('==================')
