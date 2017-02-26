'''
Created on Jan 21, 2017

@author: ubuntu
'''
x = 3
y = 5
z = 2

if x > y:
    print('x > y')
elif x > z:
    print('x > z')
else:
    print('x < y && x < z')
    
if x == y:
    print('x == y')    
elif x == z:
    print('x == z')
else:
    print('x != y && x != z')
    
if x == y:
    print('x == y')    
elif x == z:
    print('x == z')
elif y == z:
    print('y == z')
elif x < y:
    print('x < y')
elif z < y:
    print('z < y')
else:
    print('x != y && x != z')