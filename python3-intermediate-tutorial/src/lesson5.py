'''
Created on Apr 08, 2017

Timeit Module - Intermediate Python Programming p.6 
https://www.youtube.com/watch?v=Fw7u3fKFDqI&index=6&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_

@author: ubuntu
'''
#generator
# input_list = range(100)
# 
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#  
# xyz = list(i for i in input_list if div_by_five(i))

# list comprehension
# input_list = range(100)
#  
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
# 
# xyz = [i for i in input_list if div_by_five(i)]

# import timeit
# print(timeit.timeit('1+3', number=500000))

## ----------------------------------------------------- 100 items
# 0.7606023349999305
# print(timeit.timeit('''
# input_list = range(100)
#  
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#  
# xyz = list(i for i in input_list if div_by_five(i))
#     ''', number=50000))


# 0.6460088580006413
# print(timeit.timeit('''
# input_list = range(100)
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
# xyz = [i for i in input_list if div_by_five(i)]
# ''', number=50000))

## ----------------------------------------------------- 500 items

# 3.3568059429999266
# print(timeit.timeit('''
# input_list = range(500)
#   
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#   
# xyz = list(i for i in input_list if div_by_five(i))
#     ''', number=50000))


# 3.1567066879997583
# print(timeit.timeit('''
# input_list = range(500)
# 
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
# 
# xyz = [i for i in input_list if div_by_five(i)]
# ''', number=50000))

## experiments

# 0.03064402600102767
# print(timeit.timeit('''
# input_list = range(500)
#    
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
# 
# xyz = (i for i in input_list if div_by_five(i))
#     ''', number=50000))


# 3.192744396001217
# print(timeit.timeit('''
# input_list = range(500)
#  
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#  
# xyz = [i for i in input_list if div_by_five(i)]
# ''', number=50000))