'''
Created on May 21, 2017

Monte Carlo Simulation and Python 8 - Graphing Results 
based on https://www.youtube.com/watch?v=EIAa-wVazf0&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0&index=8

@author: ubuntu
'''
import random
import matplotlib
import matplotlib.pyplot as plt
import time

sampleSize = 100

startingFunds = 10000
wagerSize = 100
wagerCount = 1000

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

def doubler_bettor(funds,initial_wager,wager_count,color):
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

    plt.plot(wX,vY,color)

def simple_bettor(funds,initial_wager,wager_count,color):
    global broke_count
    
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

            if value < 0:
                currentWager += 10000000000000000
                broke_count += 1
        currentWager += 1
        
    plt.plot(wX,vY,color)

x = 0
broke_count = 0
while x < 1000:             
    simple_bettor(startingFunds,wagerSize, wagerCount,'k')
    doubler_bettor(startingFunds,wagerSize*2, wagerCount, 'c')
    x+=1
#print(('death rate:',(broke_count/float(x)) * 100))
#print(('survival rate:',100 - ((broke_count/float(x)) * 100)))
plt.axhline(0, color = 'r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()