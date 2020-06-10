# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:28:14 2020

@author: James

Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

Example:

checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False

"""

def checkio(words: str) -> bool:
    
    number_of_words = 0            # a counter for consecutive words
     
    for word in words.split():         # loop through the list of words split at spaces
        number_of_words = (number_of_words + 1) * word.isalpha()
        print(word + ' ' + str(number_of_words))
        if number_of_words == 3: return True   # if the counter is 3 set True and break
    else: return False                 


if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))               # should return True
    print(checkio("Hello World hello"))               # should return True
    print(checkio("He is 123 man"))                   # should return False
    print(checkio("1 2 3 4"))                         # should return False
    print(checkio("bla bla bla bla"))                 # should return True
    print(checkio("Hi"))                              # should return False
    print(checkio("Start 5 one two three 7 end"))     # should return True