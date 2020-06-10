# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:39:09 2020

@author: James
"""

def is_even(number):
    
    if number % 2 == 0:
        even = True
        
    if number % 2 != 0:
        even = False
        
    return even

print(is_even(8))
print(is_even(7))
print()

def is_even(number):
    return number % 2 == 0

print(is_even(8))
print(is_even(7))
print()
        

"""
def is_prime(n):
	if n == 0:
		return False
	if n == 1:
		return False
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1
	return True

"""

def is_prime(n):
    	
    for i in range(2, abs(n)):
        print(i)
        if n < 2 or n % i == 0:
            return False
    return True

print(is_prime(9))
print(is_prime(31))
print(is_prime(-3))
print(is_prime(0))
print(is_prime(1))

###################################

def is_prime(n):
    	
    for i in range(2, abs(n)):
        print(i)
        if n < 2 or n % i == 0:
            return False
    return True

print(is_prime(9))
print(is_prime(31))
print(is_prime(-3))
print(is_prime(0))
print(is_prime(1))