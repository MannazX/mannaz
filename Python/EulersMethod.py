# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:49:31 2018

@author: Andreas Larsen
"""

from matplotlib import pyplot as plt
import math

# Returns the slope of the function
def slope(yn,r,Tamb):
     dy = -r*(yn - Tamb)
     return(dy)

def euler(x,y,h,r,Tamb):
    yl=[]    # All values of y expressed as a list - Used for plotting y-coordinate of the numeric solution
    gl=[]    # All values of g expressed as a list - Used for plotting y-coordinate of the real solution
    i=[]    # All values of i expressed as a list - Used for plotting x-coordinate
    C = -((-y + Tamb)/math.e**(-r*x))    # Calculates C for the real solution
    while x < 100:
        y +=  h * slope(y,r,Tamb)                    # Calculates the next value of y
        yl.append(y)                            # Adds y to the list of all y's
        g = C*math.e**(-r*x) + Tamb             # Calculates the real solution
        gl.append(g)                            # Adds g to the list of all g's 
        i.append(x)                             # Adds x to the list of all x's
        x += h                                  # Increments x with the step lenght    
    plt.plot(i,yl, linestyle="dashed")      # Plots (x,y) for the numeric solution
    plt.plot(i,gl)                          # Plots (x,y) for the real solution
    

euler(0,100,1,0.1,23)
# =============================================================================
# euler(x,y,h,r,Tamb) 

# y    # Initial value of y
# x    # Initial value of x
# h    # Step lenght
# r    # Heat permeability
# Tamb # Ambient temperature
# =============================================================================