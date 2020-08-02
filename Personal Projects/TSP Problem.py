# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:29:15 2020

@author: James
"""
import math


def length(n1, n2):
    """Compute the distance between two nodes"""
    return math.sqrt( (n1.x - n2.x)**2 + (n1.y - n2.y)**2 )
