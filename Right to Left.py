# -*- coding: utf-8 -*-
"""
Created on Sat May 16 04:11:42 2020

@author: James
"""

def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    phrase_list = []
    for phrase in phrases: # loop through phrases
        phrase = phrase.replace("right", "left") # change instances of right to left
        phrase_list.append(phrase) # add changed phrase to list
                                    # we need to use a list becaue tuples are immutable
    
    output = ",".join(phrase_list) # join phrase list into string with ','
    return output
        

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")