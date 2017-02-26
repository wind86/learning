'''
Created on Jan 22, 2017

@author: ubuntu
'''
fileData = open('demo.txt','r').read()
print(fileData)

print('=====')

fileLines = open('demo.txt', 'r').readlines()
print(fileLines)