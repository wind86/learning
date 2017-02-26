'''
Created on Jan 22, 2017

@author: ubuntu
'''
x = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,3,6,8,2,5,1]
x.append(2)
print(x)

x.insert(2, 99)
print(x)

x.remove(2) # removes the first occurrence of 2
print(x)

x.remove(x[2]) # removes the third element
print(x)

print(x[1:3]) # slice starting from the second element to the third element

print(x[-1]) # access the last element

print(x.index(99))

print(x.count(9)) # count how many such elements are inside the list

x.sort()
print(x)

y = ['Janet','Jessy','Kelly','Alice','Joe','Bob']
y.sort()
print(y)