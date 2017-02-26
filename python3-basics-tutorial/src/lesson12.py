'''
Created on Jan 21, 2017

@author: ubuntu
'''
x = 5

def example():
    #global x
    globalx = x
    print(globalx)
    globalx+=1
    return globalx
    
x = example()
print(x)