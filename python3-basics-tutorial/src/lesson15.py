'''
Created on Jan 22, 2017

@author: ubuntu
Note: originally file is created in lesson14.py and here only appending some new data to existing file
'''
text = '\nSome additional text to append'
file = open('demo.txt','a')
file.write(text)
file.close()