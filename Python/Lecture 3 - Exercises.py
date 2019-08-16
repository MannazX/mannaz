# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:41:39 2018

@author: magge
"""
1.3
#Can a newborn baby in Norway expect to live for 10^9 seconds?

tsec = 10**9
tmin = 1/60
thr = 1/60
tday = 1/24
tyr = 1/365

tbaby = tsec*tmin*thr*tday*tyr
print(tbaby)
Ans: 31.709791983764585
#Possibly longer than 10^9 seconds

1.5
#How much will the initial 1000 dollars grown to in 3 years?
A = 1000 #Initial amount in dollars
p = 5 #Percentage interest
n = 3 #Time in years

An = A*(1 + (p/100))**n
print(An)
Ans: 1157.6250000000002


1.7
#What is the problem with the program?
from math import sin
x=1; print('sin(%g)=%g' %(x, sin(x)))
#Ans: It does not work because the person has not defined what
#to print, which is necessary for python to run it.

1.9
a.
#What are the problems in the following stated programs?
#sin^2(x) + cos^2(x) = 1 ?
from math import cos
x = pi/4
1_val = math.sin^2(x)+math.cos^2(x)
print 1_VAL
#Pi has not been imported.
#x does not need to be defined.
#Underscore is not a valid input in defining the expression.
#Wrong exponential operator used, must use **.
#Mat. is not needed for the program to be run.
from math import pi
val = (sin(x))**2 + (cos(x))**2
x = pi/4 #Not actually necessary.
print(val)
#This is how it is correctly written.

b.
#Compute s in meters
v0 =3 m/s
t =1 s
a =2 m/s**2
s = v0.t + 0,5.a.t**2
print s
#Don't use the units when running the program, it will be invalid
#syntax.
#Wrong multiplication sign used, use *.
#Wrong symbol for float number used.
v0 = 3
t = 1 
a =2
s = v0*t + 0.5*a*t**2
print(s)
#This is how it is written correctly

c.
a = 3,3
b = 5,3
a2 = a**2
b2 = b**2
eq1_sum = a2 +2*a*b + b2
eq2_sum = a2 -2*a*b + b2
print ’First equation: %g = %g’,%(eq1_sum, eq1_pow)
print ’Second equation: %h = %h’,%(eq2_pow, eq2_pow)