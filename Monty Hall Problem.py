# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:42:06 2020

@author: James
"""


import random
import matplotlib.pyplot as plt
import numpy as np

test = 1000
wins = 0
success = []

for games in range(1, test):
    the_goats = []

    the_doors = [1, 2, 3]                  # The three doors.
    
    the_car = random.randint(1,3)          # The door with the car.
    
    the_choice = random.randint(1,3)       # The first door choosen.
    
    the_goats = the_doors.copy()           # Remove the car and all that remains are goats.
    the_goats.remove(the_car)
    
    if the_goats.count(the_choice) > 0:    # The goat door can't be equal to the choice door
        the_goats.remove(the_choice)
    
    if len(the_goats) > 1:
        the_reveal = the_goats[random.randint(0, 1)]  # Reveal a goat
    else:
        the_reveal = the_goats[0]
        
    the_remaining = the_doors.copy()       # Figure out which doors remain
    the_remaining.remove(the_reveal)
    
    the_switch = the_remaining.copy()      # Switch the doors
    the_switch.remove(the_choice)
    
    if the_car == the_switch[0]:           # If the car is behind the switch door, you win!
        wins += 1
    
    success.append(wins/games)             # Calculate the average
    
                                           # Format the graph for output
plt.figure(figsize=(20,10))
plt.title('The Monty Hall Problem', fontsize=36, pad=25)
plt.xlabel('Games Played', fontsize=36)
plt.xticks(fontsize=24)
plt.grid()
plt.ylabel('Percentage Won', fontsize=36)
plt.ylim(0,1)
positions = (0, .2, .4, .6, .66, .8, 1)
labels = ('0', '20', '40', '60', '66', '80', '100')
plt.yticks(positions, labels, fontsize=24)
art.Artist.set_animated
plt.plot(success)
plt.show()