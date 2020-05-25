# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:48:38 2020

@author: James
"""

# write a funtion to test for coverage of one point X Y in a rooom
# passing the point to test and the coordinates and radius of the sensor
def test(test_x, test_y, sx, sy, sr):
    if ((test_x - sx)**2 + (test_y - sy)**2) <=sr **2:
        return True
    else:
        return False

def is_covered(room, sensors):
        
    width = room[0] # get the width of the room
    height = room[1] # get the height of the room
        
    for x in range(width):              # loop through width
        for y in range(height):         # loop through heights
            for sensor in sensors:      # loop through the list of sensors
                                        # load variables for current sensor
                sx = sensor[0]          # sensor x location
                sy = sensor[1]          # sensor y location
                sr = sensor[2]          # sensor range (radius)
                # run out rest function to determine if X and Y location
                # falls within the sensor radius
                if test(x, y, sx, sy, sr):
                    break               # if test passes, move on to next point
            else:
                return False            # if test fails terminate and return False
                        
    return True                         # if all test pass return True

if __name__ == '__main__':
    
    print("Example:")
    print(is_covered([200, 150], [[100, 75, 130]]))
    print(is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]))
    print(is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]))
 
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_covered([200, 150], [[100, 75, 130]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]]) == True
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    assert is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]]) == True
    assert is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
