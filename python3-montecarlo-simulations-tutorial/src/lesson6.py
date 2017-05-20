'''
Created on May 20, 2017

Monte Carlo Simulation and Python 6 - Bettor Statistics 
based on https://www.youtube.com/watch?v=nrkT06sVojE&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0&index=6

@author: ubuntu
'''
import random
import matplotlib
import matplotlib.pyplot as plt

broke_count = 0
xx = 0

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    else:
        return True

def doubler_bettor(funds,initial_wager,wager_count):
    global broke_count
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1

    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    broke_count += 1
                    currentWager += 10000000000000000
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    currentWager += 10000000000000000
                    broke_count += 1

        currentWager += 1

    plt.plot(wX,vY)

while xx < 1000:
    doubler_bettor(10000,100,1000)
    xx+=1

print('death rate:',(broke_count/float(xx)) * 100)
print('survival rate:',100 - ((broke_count/float(xx)) * 100))
plt.axhline(0, color = 'r')
plt.show()