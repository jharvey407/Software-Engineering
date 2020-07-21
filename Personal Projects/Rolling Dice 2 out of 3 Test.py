# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:35:33 2020

@author: James
"""


import random
import matplotlib.pyplot as plt
import matplotlib.artist as art
import numpy as np

games_won = 0                      # We start with 0 games won.
avg_won = []                       # A list to store our averages to graph.

for games in range(1, 500):        # Run the game 500 times
    roll = random.randint(1,6)     # Generate a random number between 1 and 6 inclusive.
    if roll >=1 and roll <=4:      # If the number is between 1 and 4 inclusive, you win.
        games_won += 1             # Increment the number of games won by 1.
    try:                           # Try statement avoids a divide by 0 error.
        average = games_won/games  # Calculate our average based on games won divided by games played.
    except:
        pass
    avg_won.append(average)        # Append our new average to our list.

                                   # Format out output Graph
plt.figure(figsize=(20,10))
plt.title('Rolling 1 thru 4 on a Six Sided Die', fontsize=36, pad=25.0)
plt.xlabel('Games Played', fontsize=36)
plt.xticks(fontsize=24)
plt.grid()
plt.ylabel('Percentage Won', fontsize=36)
plt.ylim(0,1)
positions = (0, .2, .4, .6, .66, .8, 1)
labels = ('0', '20', '40', '60', '66', '80', '100')
plt.yticks(positions, labels, fontsize=24)
art.Artist.set_animated


plt.plot(avg_won)
plt.show()                        # Display the Graph