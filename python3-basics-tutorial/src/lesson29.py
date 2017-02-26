'''
Created on Jan 29, 2017

@author: ubuntu
'''
dict = {'Andrew':22,'Kate':20,'John':25,'Karen':24}
print(dict)

print(dict['Kate'])

dict['Bob'] = 18
print(dict)

dict['Bob'] = 19
print(dict)

del dict['Bob']
print(dict)

dict1 = {'Andrew':[22,'blonde'],'Kate':[20,'red'],'John':[25,'brown'],'Karen':[24,'black']}
print(dict1['John'][1])