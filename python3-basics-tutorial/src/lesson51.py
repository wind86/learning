'''
Created on Feb 25, 2017

@author: ubuntu
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
    if pscan(x):
        print('port ', x, ' is opened')
    else:
        print('port ', x, ' is closed')