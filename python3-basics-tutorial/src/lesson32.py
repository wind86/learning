'''
Created on Jan 29, 2017

@author: ubuntu
'''
import sys

sys.stderr.write('stderr text\n')
sys.stderr.flush()
sys.stdout.write('stdout text\n')

print(sys.argv)

if len(sys.argv) > 0:
    print(sys.argv[0])