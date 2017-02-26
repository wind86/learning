'''
Created on Jan 21, 2017

@author: ubuntu
'''
def simple_addition(num1, num2):
    print('num1:', num1)
    print('num2:', num2)
    answer = num1 + num2
    print(answer)
    
simple_addition(3,5)
print('=====')
simple_addition(5,3)
print('=====')
simple_addition(num2=3, num1=5)
print('=====')
# should throw error
simple_addition(3,5,2)