# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:29:54 2018

@author: magge
"""

print("Converts Celcius to fahrenheit")
s = input("C= ")
C = float(s)
F = (9.0/5)*C + 32
print("is {:.2f} degrees Fahrenheit".format(F))

print("Determines the molarity of the solution")
k = input("n= ")
i = input("v= ")
n = float(k)
v = float(i)
C = n/v
print("The solution is {:.2f} mol/L".format(C))


####
formular = input("write a formular f involving x: ")

code = """
def f(x):
    return %a
""" % formular

exec(code)