# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:08:23 2018

@author: magge
"""

Cdegrees = []
for i in range(0,21):
    C = -20+2.5*i
    Cdegrees.append(C)
Cdegrees

Cdegrees = range(-20, 45, 5)
Fdegrees = [(9.0/5.0)*C+32 for C in Cdegrees]
tab1 = [Cdegrees, Fdegrees]
tab1
tab2 = [[C,F] for C,F in zip(Cdegrees, Fdegrees)]
tab2
tab3 = zip(Cdegrees, Fdegrees)
tab3

for i in range(len(Cdegrees)):
    print("%5.1f %5.1f" \
          % (Cdegrees[i], Fdegrees[i]))
    
for C,F in zip(Cdegrees, Fdegrees):
    print("%5.1f %5.1f" % (C,F))