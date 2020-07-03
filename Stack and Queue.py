# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:11:03 2020

@author: James
"""


class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self, item):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
def palindrom_checker(string):
    
    stack = Stack()
    queue = Queue()
    
    for char in string:
        stack.push(char)
        queue.enqueue(char)
        
    for i in range(len(string)):
        if stack.pop() != queue.dequeue(i):
            return False
        
    return True
    
    
string = 'springboard'
print(palindrom_checker(string))
string = 'racecar'
print(palindrom_checker(string))