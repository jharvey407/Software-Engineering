# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 07:12:51 2020

@author: James
"""

# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#


def stringAnagram(dictionary, query):
    # Write your code here
    anagrams = []                               # Empty list for output
    for word in query:                          # For each word
        an_count = 0                            # Start count at 0
        for string in dictionary:               # Test against each string
            if len(word) == len(string):        # If the lengths are differnt exit
                for char in word:               # Check if each char is in the string
                    if char not in string:      # If it's not
                        break                   # Exit the loop
                    else:
                        an_count += 1           # Else it's an anagram increment the count
        anagrams.append(an_count)               # At the end of the dictionary add the number to the list
    return(anagrams)                            # Return the list
           
# Test 1
dictionary = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on']
query = ['two', 'bca', 'no', 'listen']
print(stringAnagram(dictionary, query))
# The final answer is [2, 1, 2, 3].

# Test 2
dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']
print(stringAnagram(dictionary, query))
# The final answer is [3, 2, 0].

# Test 3
dictionary = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']
query = ["a", "nark", "bs", "hack", "stair"]
print(stringAnagram(dictionary, query))
# The final answer is [2, 2, 0, 3, 1].