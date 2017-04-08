'''
Created on Apr 08, 2017

Args and Kwargs
https://www.youtube.com/watch?v=gZB_ENJD34E&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=25

@author: ubuntu
'''

import matplotlib.pyplot as plt

blog_1 = 'I am so awesome'
blog_2 = 'Cars are cool.'
blog_3 = 'Aww look at my cat.'

# def blog_posts(*args):
#     for post in args:
#         print(post)
        
# blog_posts(blog_1)
# blog_posts(blog_1,blog_2,blog_3)


# def blog_posts_2(regular_arg, *args):
#     print(regular_arg)
#     for post in args:
#         print(post)
# 
# blog_posts_2('My blogs:',blog_1,blog_2,blog_3)

# def blog_posts_3(**kwargs):
#     for title, post in kwargs.items():
#         print(title,post)
# 
# blog_posts_3(blog_1 = 'I am so awesome',
#              blog_2 = 'Cars are cool.',
#              blog_3 = 'Aww look at my cat.')

# def graph_operation(x, y):
#     print('function that graphs {} and {}'.format(x, y))
#     
# x = [1,2,3]
# y = [2,3,1]
# graph_me = [x,y]
# graph_operation(*graph_me)


def graph_operation(x, y):
    print('function that graphs {} and {}'.format(x, y))
    plt.plot(x,y)
    plt.show()

x = [1,2,3]
y = [2,3,1]
graph_me = [x,y]
graph_operation(*graph_me)