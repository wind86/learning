'''
Created on May 21, 2017

Monte Carlo Simulation and Python 14 - 50/50 odds 
based on https://www.youtube.com/watch?v=QGu5hUarTik&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0&index=14

@author: ubuntu
'''
import random
import matplotlib
import matplotlib.pyplot as plt
import time

sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 10000

broke_count = 0
xx = 0

def rollDice():
    roll = random.randint(1,100)
    if roll <= 50:
        return False
    else:
        return True

def multiple_bettor2(funds,initial_wager,wager_count,multiple):
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


multipleSampSize = 1000000
multiple_busts = 0.0
multiple_profits = 0.0
ROI = 0

counter = 1
while counter <= multipleSampSize:
    multiple_bettor2(startingFunds,wagerSize,wagerCount,1.75)
    counter += 1

print('Total Amount Invested:', multipleSampSize * startingFunds)
print('Total Return:',ROI)
print('Difference:',ROI-(multipleSampSize * startingFunds))
print('Bust Rate:',(multiple_busts/multipleSampSize)*100.00)
print('Profit Rate:',(multiple_profits/multipleSampSize)*100.00)