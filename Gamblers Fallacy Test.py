# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 05:07:08 2020

@author: James

Testing the Gambler's Fallacy
"""
import random

results = [] # Empty list for storing the results
flips = []   # Empty list for testing
run = 0
total_flips = 0

while len(results) < 1000:
    while run < 10:
        flip = random.randint(0,1)
        total_flips += 1
        if flip == 1:
            run +=1
            flips.append(flip)
        else:
            # print('Run', run)
            run = 0
            flips = []
    else:
        # print('Run', run)
        flip = random.randint(0,1)
        total_flips += 1
        results.append(flip)
        run = 0
                
# print('Results', results)
print('Total Flips', total_flips)
print('Heads', results.count(1))
print('Tails', results.count(0))
print(results.count(1)/10, '% win')
        