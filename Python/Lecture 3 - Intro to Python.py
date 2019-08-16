# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello universe")

v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print(y)

"tekst"
print("at height t=%0.2f, the height of the ball is %0.2f m" %(t,y))

s = "At t=%0.2f, the height of the ball is %f m" %(t,y)
print(s)

some_string = 'hello'
"{:s}".format(some_string)

some_integer = 2
"{:d}".format(some_integer)

"{:10d}".format(some_integer)

"{:<10d}".format(some_integer)

"{:>10d}".format(some_integer)

some_float = .51
"{:.2f}".format(some_float)

a = 4
b = 2
c = a + b

print("{:g} + {:g} = {:g}".format(a, b, a + b))

1.0/2.0
1/2

Exponential: **
Sign: +x, -x
Multip., divis., modulo: *, /, %
Addition, subtraction: +, -

import math
x = 2.0
r = math.sqrt(x)
s = math.sin(x)
print(r)
#eller
from math import sqrt, sin
x = 2.0
r = sqrt(x)
s = sin(x)

a = (1.0/49)*49
b = (1.0/51)*51
print("{:.16f}, {:.16f}".format(a,b))

