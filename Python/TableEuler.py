# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:53:36 2018

@author: B 267.b - MAT-TEK
"""

from matplotlib import pyplot as plt
import math

def slope(yn,r,Tamb):  
    """
    Returns the slope for Newtons law of cooling 
    """                                                        
    dy = -r*(yn - Tamb)
    return(dy)

def euler(x,y,end=100,h=1,r=0.1,Tamb=23,real=False):
    """
    Calculates the approximated values, using the forward Euler Method, for Newtons law of cooling.
    The function takes the following inputs:
        
    euler(x,y,end,h,r,Tamb) 
        
    y    # Initial value of y (float or integer)
    x    # Initial value of x (float or integer)
    end  # Optional -- Last value of x (float or integer) -- Default = 100 
    h    # Optional -- Step lenght (float or integer) -- Default = 1
    r    # Optional -- Heat permeability (float or integer) -- Default = 0.1
    Tamb # Optional -- Ambient temperature (float or integer) -- Default = 23
    """

    C = -((-y + Tamb)/math.e**(-r*x))                                          # Calculates C for the real solution
    print("{:<10}{:<15}{:<15}{:<15}".format("x","y-Euler","y-Eksakt","Diff"))  # Prints the text nicely formatted
    counter =0                                                                 # Used to seperate the loop for the first point and the rest.
    while x < end+1:                                                           # Run a loop while x is less than y
        if counter < 1:                                                        # Makes sure that the first y-value of y-Euler = y-Eksakt
            g = C*math.e**(-r*x) + Tamb                                        # Calculates the real solution
            diff = g-y                                                         # Calculates the difference between y-Euler and y-Eksakt, which should be 0
            print("{:<10,g}{:<15,.4f}{:<15,.4f}{:<10,.4f}".format(x,y,g,diff)) # Prints the values nicely formatted
            counter += 1                                                       # Makes counter > 0 since we only need it for the first points
        else:
            y +=  h * slope(y,r,Tamb)                                          # Calculates the next value of y
            g = C*math.e**(-r*x) + Tamb                                        # Calculates the real solution
            diff = g-y                                                         # Calculates the difference between y-Euler and y-Eksakt
            print("{:<10,g}{:<15,.5f}{:<15,.5f}{:<15,.5f}".format(x,y,g,diff)) # Prints the values nicely formatted
        x += h                                                                 # Increments x with the step lenght
        
euler(0,100,25,0.1)                                                             # euler(x_start,y_start,x_stop,h)  