# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:39:09 2020

@author: James
"""



def is_prime(n):
    
    import math
    
    if n < 2: return False
	
    for i in range(2, (int)(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(is_prime(9))
print(is_prime(31))
print(is_prime(-3))
print(is_prime(0))
print(is_prime(1))
print('-------------------')
print()

for test in range(102):
    if is_prime(test):
        print(test, " is a prime number.")

