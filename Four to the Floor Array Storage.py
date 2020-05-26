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
        
    length = room[0] # get the width of the room
    width = room[1] # get the height of the room
    coverage = None
    array = []
        
    for x in range(length):                 # loop through width
        sensor_list = []    
        for y in range(width):              # loop through heights
            for sensor in sensors:          # loop through the list of sensors
                                            # load variables for current sensor
                sx = sensor[0]              # sensor x location
                sy = sensor[1]              # sensor y location
                sr = sensor[2]              # sensor range (radius)
                
                # run out rest function to determine if X and Y location
                # falls within the sensor radius
                if test(x, y, sx, sy, sr):
                    coverage = True
                    sensor_list.append('X') # and X to the coverage array row                   
                    break                   # if test passes, move on to next point
            else:
                coverage = False            # if test fails coverage = False
                sensor_list.append('O')     # add O to the coverage array row
        array.append(sensor_list)           # add coverage array row to array
    
    for list in array:                      # print the array
        line = ''
        for item in list:
            line += item + ' '
        print(line)    
            
        
    return coverage                         # return our coverage test results

if __name__ == '__main__':
    
    print("Example:")
    print(is_covered([15, 11], [[5,5,5]]))

    """
    print(is_covered([200, 150], [[100, 75, 130]]))
    print(is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]))
    print(is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]))
    """
   