# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:32:26 2020

@author: James
"""


def minion_game(string):

    vowels = 'AEIOU'
    s = string.upper()
    kevinsc = 0
    stuartsc = 0

    for i in range(len(s)):
        if string[i] in vowels:
            kevinsc += (len(s)-i)
        else:
            stuartsc += (len(s)-i)

    if kevinsc > stuartsc:
        print('Kevin', kevinsc)
    elif stuartsc > kevinsc:
        print('Stuart', stuartsc)
    else:
        print('Draw')

minion_game('banana')