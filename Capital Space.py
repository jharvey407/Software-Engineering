# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:25:07 2020

@author: James
"""


def cap_space(txt):
    
output = ''

    for character in txt:
        if character.isupper():
            output += ' '
            output += character.lower()
        else:
            output += character
        
return(output)