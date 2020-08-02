# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 07:03:57 2020

@author: James
"""

# Simple class Circle to provide a formula for calculating area

class Circle:    # Define the class
  pi = 3.14      # Define a local variable to be used by the class
  def area(self, radius): # Define a method called area to calculate the area
    return self.pi * radius ** 2 # Return the calculation of the area

circle = Circle() # Create an instance of Circle and save it to the variable
                  # circle

pizza_area = circle.area(6)
print(pizza_area)

teaching_table_area = circle.area(18)
print(teaching_table_area)

round_room_area = Circle().area(11460/2) # This syntax will also work
print(round_room_area)