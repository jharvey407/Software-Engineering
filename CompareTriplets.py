# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:35:33 2020

@author: James
"""


def compareTriplets(a, b):
    
    ap = 0 # Alice's points
    bp = 0 # Bob's points
    output = [] # empty list for output
    
    for index in range(3): 
        if a[index] > b[index]: ap += 1 # if Alice's score is higher add 1
        elif b[index] > a[index]: bp += 1 # Otherwise Bob'score is higher add 1
        
    output.append(ap) # add Alice's score to output
    output.append(bp) # add Bob's score to output
    return output


       
print(compareTriplets([17, 28, 30],[99, 16, 8]))
print(compareTriplets([5, 6, 7],[3, 6, 10])) 