'''
Created on Jan 22, 2017

@author: ubuntu
'''
text = 'Some title\nSome text'
file = open('demo.txt','w')
file.write(text)
file.close()