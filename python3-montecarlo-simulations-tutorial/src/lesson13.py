'''
Created on May 21, 2017

Monte Carlo Simulation and Python 13 - D'Alembert Strategy 
based on https://www.youtube.com/watch?v=w43uNAaF1hU&index=13&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0

@author: ubuntu
'''
import random
import matplotlib
import matplotlib.pyplot as plt
import time

#lower_bust = 31.235
#higher_profit = 63.208

lower_bust = 19.00
higher_profit = 69.00


sampleSize = 10000
startingFunds = 10000
wagerSize = 100
wagerCount = 10000

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

def dAlembert(funds,initial_wager,wager_count):#,color):

    global da_busts
    global da_profits
    
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

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
                if value <= 0:
                    da_busts += 1
                    break
        elif previousWager == 'loss':
            wager = previousWagerAmount + initial_wager
            if (value - wager) <= 0:
                wager = value
            
            if rollDice(): 
                value += wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    da_busts += 1
                    break

        currentWager += 1

    if value > funds:
        da_profits+=1


def multiple_bettor(funds,initial_wager,wager_count):
    global multiple_busts
    global multiple_profits
    
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
                if value <= 0:
                    multiple_busts += 1
                    break
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * random_multiple
                if (value - wager) <= 0:
                    wager = value
                    
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * random_multiple
                if (value - wager) <= 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    multiple_busts += 1
                    break

        currentWager += 1

    if value > funds:
        multiple_profits+=1

x = 0
while x < 1:
    
    da_busts = 0.0
    da_profits = 0.0
    daSampSize = 10000
    currentSample = 1
    
    while currentSample <= daSampSize:
        dAlembert(startingFunds,wagerSize,wagerCount)
        currentSample += 1

    if ((da_busts/daSampSize)*100.00 < lower_bust) and ((da_profits/daSampSize)*100.00 > higher_profit):
        print('#################################################')
        print('Lower Bust Rate Than:',lower_bust)
        print('Higher profit rate than:',higher_profit)
        print('Bust Rate:',(da_busts/daSampSize)*100.00)
        print('Profit Rate:',(da_profits/daSampSize)*100.00)
        print('#################################################')
        time.sleep(5)
    else:

        print('####################################')
        print('To beat:')
        print('Lower Bust Rate Than:',lower_bust)
        print('Higher profit rate than:',higher_profit)
        print('Bust Rate:',(da_busts/daSampSize)*100.00)
        print('Profit Rate:',(da_profits/daSampSize)*100.00)
        print('####################################')

    x+=1