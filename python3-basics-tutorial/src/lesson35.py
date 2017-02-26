'''
Created on Jan 29, 2017

@author: ubuntu
'''
import urllib.request
#import urllib.parse

#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())

'''
url = 'http://pythonprogramming.net'
values = {'s':'basic','submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
res = urllib.request.urlopen(req)

resData = res.read()
print(resData)
'''

''' failing with 403 status code
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))
'''

try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
    
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    
    resData = res.read()
    
    saveFile = open('lesson33_googlesearchresponse.txt','w')
    saveFile.write(str(resData))
    saveFile.close()
    
except Exception as e:
    print(e)