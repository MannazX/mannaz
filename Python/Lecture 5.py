# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 08:17:36 2018

@author: magge
"""

def F(C):
    return(9.0/5.0)*C + 32
    print(F)

c = 10.0
F1 = F(c)
print(F1)
print(F(10.0)) #is the same as print(F1)
#50.0 is float, because a float expression is in the code.

C = 20.0

def F(C):
    return (9.0/5.0)*C + 32

def FF():
    return (9.0/5.0)*C + 32

print("F(10.0) = %.2f, FF() = %.2f" \
      % (F(10.0), FF())) #F(10.0) = 50.00, FF() = 68.00

a = 20; b = -10.0

def f1(x):
    a = 21
    return a*x +b

def f2(x):
    global a
    a = 21
    return a*x + b

print(f1(3) ,a); #53.0 20
print(f2(3) ,a); #53.0 21

F = 32

def C(F):
    return (5.0/9.0)*(F - 32)

print("C(32) = %.1f" \ 
      % (C(32)))#remember to specify float when formatting

def yfunc(t, v0):
    g = 9.81
    return v0*t - 0.5*g*t**2

y = yfunc(0.1, 6)
y = yfunc(0.1, v0=6)
y = yfunc(v0=6, t=0.1)
print(y)

def yfunc(t, v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt
print(yfunc(2, 5))

pos, vel = yfunc(0.1, 6)

def yfunc(t, v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt

r = yfunc(0.1, 6)
pos = r[0]
vel = r[1]

d e f print_yfunc (t , v0 ) :
pos , vel = yfunc (t , v0 )
print("At t =%0.2f[s] and v0 =%0.2 f [m/s], y(t) =%0.2f[m] and \
y ’( t ) ) =%0.2 f [ m / s ]" % (t , v0 , pos , vel ) )
#returns nothing

# f(t; A, a, omega) = Ae^(-at)*sin(omega*t)
from math import pi, exp, sin

def f(t, A=1, a=1, omega=2*pi):
    return A*exp(-a*t)*sin(omega*t)

print(f)

v1 = f(0.2)
v2 = f(0.2, omega=1)
v3 = f(0.2, A=2, a=0.5, omega=2*pi*4)
v4 = f(0.2, 2, 0.5, 2*pi*4)#same as v3

print(v1)
print(v2)
print(v3)
print(v4)

def m(rho):
    V = 1000
    return V*rho
print(m(1.3)) #1300

def num_diff(f, x, h=1E-6):
    return (f(x+h) - f(x-h))/(2*h)
    
def g(x):
    return x**(-6)

x = 1.2
print("Num. approx. of g'(%.2f) is %.2f"
      % (x, num_diff(g, x)))
#Num. approx. of g'(1.20) is -1.67

#Lambda functions
f = lambda x: x**2 + 4

def f(x):
    return x**2 + 4

dg = num_diff(lambda x: x**(-6), 1.2)
print(dg) #-1.674489883279895

def f(x):
    if 0 <= x <= pi:
        return sin(x)
    else:
        return 0.0

if condition:
    a = value1
else:
    a = value2

a = (value if condition else value2)

def f(x):
    return (sin(x) if 0 <= x <= pi else 0)

f = lambda x: (sin(x) if 0 <= x <= pi else 0)

