'''
Created on Feb 25, 2017

@author: ubuntu
'''
from ftplib import FTP


ftp = FTP('domainname.txt')
ftp.login(user="username", passwd="pass")
ftp.cwd("some-directory")

def grabFile():
    filename = 'filename.txt'
    localfile = open(filename, 'rb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    filename = 'filename.txt'
    ftp.storlines('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()