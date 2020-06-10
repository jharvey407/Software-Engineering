# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:32:26 2020

@author: James
"""
import re

string = 'BANANA'
vowels = ['A', 'E', 'I', 'O', 'U']

vowel_word = []
con_word = []



for index in range(len(string)):
    for vowel in vowels:
        print(vowel)
        if string[index] == vowel:
            print(string[index])
            vowel_word.append(string[index:])
            print(vowel_word)
        