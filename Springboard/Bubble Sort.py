# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 06:49:03 2020

@author: James
"""
# First test commit

def bubbleSort(lst):
    for j in range(len(lst)):
        for i in range(1,len(lst)):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
    return(lst)

test0 = [3, 22, 14, 434, 501, 11, 9, 1230, 304, 123, 5412, 381923, 302, -3, 1]
 
test1 = [43, 12, 7, 9, 22, 1, 104]
 
test2 = [100, 0, 0, -20, 30, -5]
 
test3  = [28, 4, 17, 666, 1001, 52, 61, 30]

print(bubbleSort(test0))
print(bubbleSort(test1))
print(bubbleSort(test2))
print(bubbleSort(test3))