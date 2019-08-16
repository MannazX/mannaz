# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 13:33:12 2018

@author: magge
"""

#Værdigerne i det kinematiske system
v0 = 15
g = 9.82
n = 20
delta = (2*v0/g)/n

#Listerne for t og y
t = []
for idx in range(0, n+1):
    t.append(idx*delta)
    #print(t) 
y = [v0*T - 0.5*g*T**2 for T in t]
#print(y)

#De to lister traverset med et for loop
for i in range(len(t)):
    print("%5.1f %5.1f" \
          % (t[i], y[i]))
