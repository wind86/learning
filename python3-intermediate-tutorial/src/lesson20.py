'''
Created on Apr 08, 2017

Special Methods, OOP, and Iteration Python Tutorial
https://www.youtube.com/watch?v=jucLTJCM5jA&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=21

@author: ubuntu
'''


# x = range(5)
# 
# x = (i for i in range(5))
# 
# for i in x:
#     print(i)
#     
    
# x = (i for i in range(5))
# next(x)
# next(x)
# for i in x:
#     print(i)
    
# x = (i for i in range(5))
# x.__next__()
# x.__next__()
# for i in x:
#     print(i)

#print(dir(x))

#print(dir(range))


class range_examp:
    
    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val
        
# for i in range_examp(5):
#     print(i)
#     
    
# i = range_examp(5)
# 
# i.__next__()
# i.__next__()
# 
# for j in i:
#     print(j)
    
    
#print(dir(range_examp))


def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1
         
# for i in range_gen(5):
#     print(i)

print(dir(range_gen(5)))