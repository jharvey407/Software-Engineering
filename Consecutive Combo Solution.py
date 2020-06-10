# -*- coding: utf-8 -*-
"""
Created on Sun May 17 07:20:40 2020

@author: James
"""

def consecutive_combo(lst1, lst2):
    
    lst3 = lst1 + lst2  # combine the lists
    lst3.sort()         # sort the list
    
    for index in range(len(lst3)-1):             # loop through list                                                     
        if (lst3[index + 1] - lst3[index]) > 1:  # if the difference between this number and the next
            return False                         # is greater than 1 they are not consecutive
    else:
        return True
    
  
print(consecutive_combo([7, 4, 5, 1], [2, 3, 6])) # True

print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])) # False

print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])) # False

print(consecutive_combo([44, 46], [45])) # True    