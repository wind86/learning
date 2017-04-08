'''
Created on Apr 08, 2017

Object Oriented Programming Introduction - Intermediate Python Programming p.13 
https://www.youtube.com/watch?v=ekA6hvk-8H8&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=13

@author: ubuntu
'''

import random

class Blob:
    
    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color
        
    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y
        
        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH
        
        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT