# -*- coding: utf-8 -*-
"""
Created on Wed May 27 05:06:48 2020

@author: James
"""


def Factorial(num):
    
    if num > 1:
        return num * Factorial(num-1)
    
    
    else:
        return num
    
print(Factorial(5))    
    
# 5*4*3*2*1 = 120