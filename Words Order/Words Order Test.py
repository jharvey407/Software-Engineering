# -*- coding: utf-8 -*-
"""
Created on Thu May 28 04:58:57 2020

@author: James
"""


# words order

def words_order(text: str, words: list) -> bool:
    
    print('begin')
    print('text:', text)
    print('words:', words)
    test_words = text.split()
    print('test words:', test_words)
    found_words = []
                
    for word in test_words:
        print('word to test for:', word)
        
        if word in words:
            print('found word', word)
            found_words.append(word)
            print('found words:', found_words)
            
      
    print()        
    print('words', words)
    print('found', found_words)
    print()       
            
    if words == found_words:
        return True         
    
    return False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))
    print()
    print(words_order('hi world im here', ['world']))
    print()
    print(words_order('hi world im here', ['here', 'world']))
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
 