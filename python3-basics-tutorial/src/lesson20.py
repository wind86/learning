'''
Created on Jan 22, 2017

@author: ubuntu
'''
example_list = [2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,8,7,2,5,2,1,9]

'''
# importing dependency 1
import statistics as s

print('stdev:',s.stdev(example_list))
print('variance:',s.variance(example_list))
'''

'''
# importing dependency 2
from statistics import stdev, variance

print('stdev:',stdev(example_list))
print('variance:',variance(example_list))
'''

'''
#importing dependency 3
from statistics import stdev as std, variance as var

print('stdev:',std(example_list))
print('variance:',var(example_list))
'''

#importing dependency 4
from statistics import *

print('stdev:',stdev(example_list))
print('variance:',variance(example_list))
