'''
Created on Apr 08, 2017

Decorators in Python Tutorial
https://www.youtube.com/watch?v=rPCeCPT-f28&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=18

@author: ubuntu
'''
from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style,str(item()))
        return wrapped_item
    return add_wrapping


@add_wrapping_with_style('horribly')
@add_wrapping_with_style('beautifully')
def new_gpu():
    return 'a new Tesla P100 GPU!'

print(new_gpu())