# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:39:09 2020

@author: James
"""



def is_prime(n):
    
    for i in range(2, n):  # loop through numbers from 2 and test
        if n % i == 0:     # if it is divisible than it's not prime
            return False
    return n > 1

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

