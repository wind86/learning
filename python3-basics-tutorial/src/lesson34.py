'''
Created on Jan 30, 2017

@author: ubuntu
'''
import re

exampleString = '''Jessica is 16 years old, Daniel is 27 years old,
Edgar is 56 years old and his father Roy is 87'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z]{1}[a-z]*', exampleString)

print(ages)
print(names)

dictionary = {}
for x in range(0, len(ages)):
    dictionary[names[x]] = ages[x]
    
print(dictionary)