# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 08:17:54 2018

@author: magge
"""

print("Converts Celsius to Fahrenheit")
s = input("C= ")
C = float(s)
F = (9.0/5)*C + 32
print("is {:.2f} degrees Fahrenheit".format(F))
#C= (type a number here and enter to compute in Fahrenheit)



print("Add two inputs")
i1 = eval(input("Input 1: ")) #Input 1: 4
i2 = eval(input("Input 2: ")) #Input 2: 6
r = i1 + i2 #Sum = 10, type = <class 'int'>
print("Sum = {0}, type = {1}".format(r, type(r)))

