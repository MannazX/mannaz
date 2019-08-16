# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:53:31 2018

@author: magge
"""

#3.8
from math import sqrt 
def roots(a, b, c):
    posr = -b + sqrt(b**2 - 4*a*c)
    negr = -b - sqrt(b**2 - 4*a*c)
    return posr, negr
print(roots(-2.0, 4.0, 5.0))
#3.4833147735478827, -11.483314773547882

#3.12
def midpointint(f, a, b, n):
    h = (a - b)/n

def L(n):
    s = 0
    for i in range(1, n-1):
        s += f(a + i*h + 0.5*h)
    return s
print(L(2))
    
#3.24
from math import exp
from math import cos
from math import pi
from math import log
def num_diff(f, x, h=1E-5):
    return (f(x+h) - f(x-h))/(2*h)
#3.c
def g(x):
    return exp(x)

x = 0
print("Num. approx. of g'(%.2f) is %.2f"
      % (x, num_diff(g, x))) 
#Num. approx. of g'(0.00) is 1.00

def h(x):
    return exp(-2*(x**2))

x = 0
print("Num. approx. of h'(%.2f) is %.2f"
      % (x, num_diff(h, x)))
#Num. approx. of h'(0.00) is 0.00

def i(x):
    return cos(x)

x = 2*pi
print("Num. approx. of i'(%.2f) is %.2f"
      % (x, num_diff(i, x)))
#Num. approx. of i'(6.28) is 0.00

def j(x):
    return log(x)

x = 1
print("Num. approx. of j'(%.2f) is %.2f"
      % (x, num_diff(j, x))) 
#Num. approx. of j'(1.00) is 1.00

#3.25
def fact(n):
    f = n*(n-1)*(n-2)*(n-3)
    return f

def test_fact():
    n = 6
    
fact(1)
print(fact(n))    

#3.27
from math import cos
from math import pi
a = -pi/2
b = 2*pi
n = 1000

min_value = n*cos(a)
max_value = n*cos(b)

def maxmin(a, b, n):
    return (min_value - max_value)

print(-pi/2, 2*pi, 1000)
