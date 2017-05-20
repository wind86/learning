'''
Created on May 20, 2017

Monte Carlo Simulation and Python 3 - Simple Bettor Creation 
based on https://www.youtube.com/watch?v=1TgOQvZ88hw&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0&index=3

@author: ubuntu
'''
import random

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print(roll,'roll was 100, you lose. What are the odds?! Play again!')
        return False
    elif roll <= 50:
        #print(roll,'roll was 1-50, you lose.')
        return False
    else:
        #print(roll,'roll was 51-99, you win! *pretty lights flash* (play more!)')
        return True


'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1

    if value < 0:
        value = 'Broke!'
    print('Funds:', value)

x = 0

while x < 100:
    simple_bettor(10000,100,50)
    x += 1