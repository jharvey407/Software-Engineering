# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 06:15:17 2020

@author: James
"""


def insertionSort(lst):
    print(lst)
    # Main loop
    # Loop through all values in list starting with the second
    for i in range(1, len(lst)):
        # Second loop
        # Loop through all values in list
        
        for j in range(0,i):
            print('Test ', lst[i], '<', lst[j])
            # If current value is smaller then the test value swap values
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                print(lst)
            
        print(lst)
    return lst

test0 = [3, 22, 14, 434, 501, 11, 9, 1230, 304, 123, 5412, 381923, 302, -3, 1]
 
test1 = [43, 12, 7, 9, 22, 1, 104]
 
test2 = [100, 0, 0, -20, 30, -5]
 
test3  = [28, 4, 17, 666, 1001, 52, 61, 30]

print(insertionSort(test0))
'''print()
print(insertionSort(test1))
print()
print(insertionSort(test2))
print()
print(insertionSort(test3))
'''