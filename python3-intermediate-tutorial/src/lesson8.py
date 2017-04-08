'''
Created on Apr 08, 2017

More on Generators with Python
https://www.youtube.com/watch?v=PewCyZSrnOI&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=9

@author: ubuntu
'''

# def simple_gen():
#     yield 'Oh'
#     yield 'hello'
#     yield 'there'
#     
# for i in simple_gen():
#     print(i)

CORRECT_COMBO = (3, 6, 1)
 
# for c1 in range(10):
#     for c2 in range(10):
#         for c3 in range(10):
#             if (c1, c2, c3) == CORRECT_COMBO:
#                 print('Found the combo:{}'.format((c1, c2, c3)))

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)
                
for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)))
        break