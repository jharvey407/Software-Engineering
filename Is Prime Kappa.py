# -*- coding: utf-8 -*-
"""
Created on Sun May 17 06:26:43 2020

@author: James
"""


def is_prime(n):
  return len( set([ n%i==0 for i in range(2,n) ])) == 1

print(is_prime(2))
print(is_prime(3))
print(is_prime(0))
print(is_prime(1))

for test in range(1002):
    if is_prime(test):
        print(test, " is prime.")
    
print('-----------')   

Test.assert_equals(is_prime(0), False)
Test.assert_equals(is_prime(1), False)
Test.assert_equals(is_prime(2), True)
Test.assert_equals(is_prime(3), True)
Test.assert_equals(is_prime(4), False)
Test.assert_equals(is_prime(5), True)
Test.assert_equals(is_prime(6), False)
Test.assert_equals(is_prime(7), True)
Test.assert_equals(is_prime(8), False)
Test.assert_equals(is_prime(9), False)
Test.assert_equals(is_prime(10), False)
Test.assert_equals(is_prime(71), True)
Test.assert_equals(is_prime(72), False)
Test.assert_equals(is_prime(73), True)
Test.assert_equals(is_prime(112), False)
Test.assert_equals(is_prime(197), True)
Test.assert_equals(is_prime(5851), True)
Test.assert_equals(is_prime(7906), False)
Test.assert_equals(is_prime(7907), True)
 
"""    
def is_prime(n):
  return set([False]) == set([ n%i==0 for i in range(2,n) ])    

print(is_prime(2))
print(is_prime(3))
print(is_prime(0))
print(is_prime(1))
print()

for test in range(102):
    print(test, is_prime(test))
"""    