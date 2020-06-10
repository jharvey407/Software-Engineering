# -*- coding: utf-8 -*-
"""
Created on Tue May 26 05:49:45 2020

@author: James
"""


count = int(input())

phone_dict = {}

for entry in range(count):
    
    data = input()
    data = data.split()
    phone_dict.update({data[0]:data[1]})

while True:
    
    try:
        name = input()
        if name in phone_dict:
            number = phone_dict[name]
            print(name + '=' + number)
        else:
            print('not found')
    except:
        break