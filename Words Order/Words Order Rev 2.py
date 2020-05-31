# -*- coding: utf-8 -*-
"""
Created on Fri May 29 04:02:32 2020

@author: James
"""


# -*- coding: utf-8 -*-
"""
Created on Thu May 28 04:58:57 2020

@author: James
"""


# words order

def words_order(text, words):
    text_words = [word for word in text.split() if word in words and words.count(word) < 2]
    return words == text_words


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
 