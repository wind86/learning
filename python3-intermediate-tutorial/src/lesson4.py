'''
Created on Apr 08, 2017

More on list comp and generators - Intermediate Python Programming p.5 
https://www.youtube.com/watch?v=MJUbUDa-YCA&index=5&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_

@author: ubuntu
'''
# input_list = [5,6,2,1,6,7,10,12]
# 
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
# 
# xyz = (i for i in input_list if div_by_five(i))
# print(list(xyz))
# 
# xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)

# [print(i) for i in range(5)]
[[print(i,ii) for ii in range(3)] for i in range(5)]