# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:28:14 2020

@author: James
"""

def checkio(words: str) -> bool:
    
    word_list = words.split() # split string at spaces
    print()
    print(word_list)
    number_of_words = 0 # a counter for consecutive words
    three_words = True # default value
     
    for word in word_list: # loop through the list of words
    
        if number_of_words < 3 and three_words == True:    
            if not word.isalpha():
                three_words = False
            else:
                number_of_words +=1
        
        print(word + ' ' + str(word.isalpha()) + ' ' + str(number_of_words))
        
        if three_words == False:
            break
                 
    print('-------------')
    return three_words                 


if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))               # should return True
    print(checkio("Hello World hello"))               # should return True
    print(checkio("He is 123 man"))                   # should return False
    print(checkio("1 2 3 4"))                         # should return False
    print(checkio("bla bla bla bla"))                 # should return True
    print(checkio("Hi"))                              # should return False
    print(checkio("Start 5 one two three 7 end"))     # should return True