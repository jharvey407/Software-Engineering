# -*- coding: utf-8 -*-
"""
Created on Wed May 27 05:14:14 2020

@author: James
"""


def n_times_k(n, k):
    if n > 1:
        return k + n_times_k(n-1, k)
    else:
        return k
    
print(n_times_k(4, 5))