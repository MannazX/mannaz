# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:45:27 2018

@author: magge
"""


print("Add to inputs")
i1 = eval(input("input 1: "))
i2 = eval(input("input 2: "))
t = i1 + i2
print("Sum = {0}, type {1}".format(t, type(t)))
#With integers:
#input 1: 23
#input 2: 34
#Sum = 57, type <class 'int'>

#Now with list:
#input 1: [3.2, 4.1, 5.0, 5.9, 6.8, 7.7]
#input 2: [8.6, 9.5, 10.4, 11.3, 12.2, 13.1]
#Sum = [3.2, 4.1, 5.0, 5.9, 6.8, 7.7, 8.6, 9.5, 10.4, 11.3, 12.2, 13.1], 
#type <class 'list'>

#Now with tuples:
#input 1: (2, 4, 5)
#input 2: (3, 5, 6)
#Sum = (2, 4, 5, 3, 5, 6)

print("This is a string")
i1 = eval(input("this is a string 1: "))
i2 = eval(input("this is a string 2: "))
r = i1 + i2
print("Sum = {0}, type {1}".format(r, type(r)))