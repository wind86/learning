'''
Created on Jan 22, 2017

@author: ubuntu
'''
import statistics

example_list = [2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,8,7,2,5,2,1,9]
print('mean:',statistics.mean(example_list))
print('median:',statistics.median(example_list))
print('stdev:',statistics.stdev(example_list))
print('variance:',statistics.variance(example_list))
