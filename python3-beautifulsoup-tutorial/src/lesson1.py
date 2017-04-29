'''
Created on Apr 30, 2017

Web scraping and parsing with Beautiful Soup & Python Introduction p.1 
based on https://www.youtube.com/watch?v=aIPqt-OdmS0&index=1&list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS

@author: ubuntu
'''
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)


for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

for url in soup.find_all('a'):
    print(url.get('href'))

print(soup.get_text())