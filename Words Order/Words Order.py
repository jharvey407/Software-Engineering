# -*- coding: utf-8 -*-
"""
Created on Thu May 28 04:58:57 2020

@author: James
"""


# words order

def words_order(text: str, words: list) -> bool:
    
    for word in words:             # loop through the list of words
        if words.count(word) > 1:  # if a word appears more than once
            return False           # return False
    
    test_words = text.split() # split test string into list of words
    found_words = []          # creat list to hold words we find
                
    for word in test_words:           # loop through words in test words list
        if word in words:             # if word is in our list of words to find
            found_words.append(word)  # add it to our found word list

    if words == found_words: # of the words we found match the words we were
        return True          # testing for, return True
    
    return False             # return False if we didn't return True


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))
    print()
    print(words_order('hi world im here', ['world']))
    print()
    print(words_order('hi world im here', ['here', 'world']))
    print()
    print(words_order('hi world im here', ['world', 'world']))
    print()



    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here', ['world', 'here', 'hi']) == False
    assert words_order('hi world im here', ['world', 'im', 'here']) == True
    assert words_order('hi world im here', ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here', ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
 