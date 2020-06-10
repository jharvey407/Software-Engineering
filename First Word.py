# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:30:23 2020

@author: James
"""


def first_word(text):
    
    char_to_replace = "!@#$%^&*,." # indentify any possible extraneous characters
    for char in char_to_replace: # loop though characters and replace
        text = text.replace(char, " ")
    
    return text.split()[0] # return the fist word of the string
        
if __name__ == '__main__':
    
    print("Example:")
    print(first_word("Hello world"))
    print(first_word(" a word "))
    print(first_word("don't touch it"))
    print(first_word("greetings, friends"))
    print(first_word("hello.world"))
    print(first_word("...and..."))