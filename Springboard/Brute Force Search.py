# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:34:55 2020

@author: James
"""
def bruteForceSearch(lst, item):
    for number in lst:
        if item == number:
            return 'Found ', item
    else:
        return item, ' not found'
        

test0 = [-3, 1, 3, 9, 11, 14, 22, 123, 302, 304, 434, 501, 1230, 5412, 381923]
searchItem0 = 13

print(bruteForceSearch(test0, searchItem0))

test1 = [1, 7, 9, 12, 22, 43, 104]
searchItem1 = 9

print(bruteForceSearch(test1, searchItem1))
 
test2 = [-20, -5, 0, 0, 30, 100]
searchItem2 = 31

print(bruteForceSearch(test2, searchItem2))
 
test3 = [4, 17, 28, 30, 52, 61, 666, 1001]
searchItem3 = 666

print(bruteForceSearch(test3, searchItem3))
