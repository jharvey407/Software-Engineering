# -*- coding: utf-8 -*-
"""
Created on Tue May 26 05:10:57 2020

@author: James
"""


# Array test case

array = []

for y in range(10):
    x_list = []
    for x in range(16):
        x_list.append(x)
    array.append(x_list)    
    
for list in array:
    print(list)

print()
print(array[2][5])