# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 06:49:03 2020

@author: James
"""
# First test commit
# Second test commit, without pushing the first commit

def bubbleSort(lst):
    # Primary loop
    # Loop through the list the number of items in the list
    for j in range(len(lst)):
        # Secondary loop
        # Loop throuhg the list swapping hihger numbers with lower numbers
        for i in range(1,len(lst)):
            # Test if this number is smaller then the previous number
            if lst[i] < lst[i-1]:
                # Swap the numbers
                lst[i], lst[i-1] = lst[i-1], lst[i]
        # Output for illustration purposes
        print(lst)    
    return(lst)

test0 = [3, 22, 14, 434, 501, 11, 9, 1230, 304, 123, 5412, 381923, 302, -3, 1]
 
test1 = [43, 12, 7, 9, 22, 1, 104]
 
test2 = [100, 0, 0, -20, 30, -5]
 
test3  = [28, 4, 17, 666, 1001, 52, 61, 30]

print(bubbleSort(test0))
print()
print(bubbleSort(test1))
print()
print(bubbleSort(test2))
print()
print(bubbleSort(test3))