'''
Created on Jan 29, 2017

@author: ubuntu
'''
import os

curDir = os.getcwd()
print(curDir)

import time

os.mkdir('newdir')
time.sleep(2)

os.rename('newdir','newdir2')
time.sleep(2)

os.rmdir('newdir2')