# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:03:01 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

def converter(x,b,real):
    """
    The converter takes an integer and converts it into the a number of the
    given base. x is the number which is used for the conversion,
    b is the base for the desired conversion, q is the quotient for the
    number between x and b, r is the rest value (the values of the converted number).
    The converter runs with a loop which is designed to break when x is reduced to zero.
    The loop appends the x and r values into lists of the x and the r values.
    The r list is set to be printed in reverse order, since the loop actually
    lists the converted number in reverse order. The x and b values are set
    as intput values for the script, so that the user can easily give the
    converter the values needed for the conversion. The real input shows
    the computation steps that the loop takes when it runs.

    """
    i = 0
    x_list = []
    r_list = []
    x_list.append(x)
    while True:
        q = x/b
        d = m.ceil(x-q)
        r = x - b*(x-d)
        q = m.floor(q)
        x = m.floor(q)
        r_list.append(r)
        x_list.append(x)
        i += 1
        if real == 1:
            print("{:d} {:6d} {:8d}".format(i,x,r))
        if x == 0:
            break

    
#    print(x_list)
    print("The number is converted to base {:}".format(b))
    print("Therefor the converted base 10 number is given as:")
    #print(r_list) #this prints the reverse number
    r_list = [r_list[i] for i in range(len(r_list)-1,-1,-1)]
    for i in r_list:
        print(i, end="")
    print(10*' ')
    print(r_list)

x = int(input("Number for conversion:"))
b = int(input("Base for the conversion of the number:"))
real = int(input("For computation steps of the conversion revealed, type 1:"))
    

converter(x,b,real)
