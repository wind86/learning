'''
Created on Apr 30, 2017

Navigation with Beautiful Soup 4
based on https://www.youtube.com/watch?v=kRDrlvO-Oz0&index=2&list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS

@author: ubuntu
'''
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

nav = soup.nav

for url in nav.find_all('a'):
    print(url.get('href'))
    
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
    
for div in soup.find_all('div', class_='body'):
    print(div.text)