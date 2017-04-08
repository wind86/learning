'''
Created on Apr 08, 2017

String Concatenation and Formatting - Intermediate Python Programming p.2 
based on https://www.youtube.com/watch?v=jA5LW3bR0Us&index=2&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_

@author: ubuntu
'''

# names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# for name in names:
    #print('Hello there, ' + name)
    #print(' '.join(['Hello there', name]))
    
# print(', '.join(names))

# import os 
# 
# location_of_files = '/home/ubuntu/workspace/project/learning/python3-intermediate-tutorial/src'
# file_name = 'example.txt'
# 
# print(location_of_files + '/' + file_name)
# 
# with open(os.path.join(location_of_files, file_name)) as f:
#     print(f.read())

who = 'Gary'
how_many = 12

print(who, 'bought', how_many, 'apples today!')
print('{} bought {} apples today!'.format(who, how_many))