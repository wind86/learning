'''
Created on May 21, 2017

Monte Carlo Simulation and Python 16 - Comparing profitability 
based on https://www.youtube.com/watch?v=u9mgSk9-IOY&index=16&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0

@author: ubuntu
'''
import random
import matplotlib
import matplotlib.pyplot as plt
import time

sampleSize = 1000
startingFunds = 100000
wagerSize = 100
wagerCount = 1000


def rollDice():
    roll = random.randint(1,100)

    if roll <= 50:
        return False
    elif roll >= 51:
        return True

def dAlembert(funds,initial_wager,wager_count):
    global ROI
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

    ROI += value

def multiple_bettor2(funds,initial_wager,wager_count,multiple):#,color):
    global ROI
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
                wager = previousWagerAmount * multiple
                if (value - wager) <= 0:
                    wager = value
                    
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * multiple
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

    ROI += value

    if value > funds:
        multiple_profits+=1  


daSampSize = 100000
da_busts = 0.0
da_profits = 0.0
ROI = 0

counter = 1
while counter <= daSampSize:
    dAlembert(startingFunds,wagerSize,wagerCount)
    counter += 1

print('Total Amount Invested:', daSampSize * startingFunds)
print('Total Return:',ROI)
print('Difference:',ROI-(daSampSize * startingFunds))
print('Bust Rate:',(da_busts/daSampSize)*100.00)
print('Profit Rate:',(da_profits/daSampSize)*100.00)