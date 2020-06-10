# -*- coding: utf-8 -*-
"""
Created on Wed May 27 04:15:22 2020

@author: James
"""


def summation(num):
    if num <= 0:
        return 0
    else:
        return num + summation(num - 1)
    
print(summation(5))    
print(summation(10))
print(summation(0))
