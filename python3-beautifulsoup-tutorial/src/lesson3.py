'''
Created on Apr 30, 2017

Parsing tables and XML with Beautiful Soup 4
based on https://www.youtube.com/watch?v=sAuGH1Kto2I&index=3&list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS

@author: ubuntu
'''
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
    
import pandas as pd

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
for df in dfs:
    print(df)
    
    
source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'xml')

for url in soup.find_all('loc'):
    print(url.text)