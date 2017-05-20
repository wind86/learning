'''
Created on May 20, 2017

Monte Carlo Simulation and Python 1 - Intro 
based on https://www.youtube.com/watch?v=9M_KPXwnrlE&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0

@author: ubuntu
'''
import random

def rollDice():
    return random.randint(1,100)

x = 0
while x < 100:
    result = rollDice()
    print(result)
    x+=1