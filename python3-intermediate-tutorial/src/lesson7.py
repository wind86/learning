'''
Created on Apr 08, 2017

Python's Zip function
https://www.youtube.com/watch?v=bMxEU0iG-KA&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=8

@author: ubuntu
'''

x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

# for a,b in zip(x,y):
#     print(a,b)
    
# for a,b,c in zip(x,y,z):
#     print(a,b,c)

# print(zip(x,y,z))

# print(list(zip(x,y,z)))

names = ['Jill','Jack','Jeb','Jessica']
grades = [99,56,24,87]

d = dict(zip(names,grades))
print(d)