'''
Created on May 20, 2017

Monte Carlo Simulation and Python 4 - Plotting with Matplotlib 
based on https://www.youtube.com/watch?v=jeVZP5vgEC4&index=4&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0

@author: ubuntu
'''
import random
import matplotlib
import matplotlib.pyplot as plt

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

    wX = []
    vY = []
    currentWager = 1

    while currentWager <= wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        wX.append(currentWager)
        vY.append(value)
        currentWager += 1

    if value < 0:
        value = 'Broke!'
    #print('Funds:', value)
    plt.plot(wX,vY)

x = 0
while x < 1000:
    simple_bettor(10000,100,10000)
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()