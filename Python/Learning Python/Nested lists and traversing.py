# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:33:19 2019

@author: magge
"""

Cdeg = range(-10,20,5)
Fdeg = [(9.0/5.0)*C+32 for C in Cdeg]

tab1 = [Cdeg,Fdeg]
tab2 = [[C,F] for C,F in zip(Cdeg,Fdeg)]
tab3 = zip(Cdeg,Fdeg)

for C,F in tab3: #tab3 is zip of Cdeg and Fdeg
    print("%5.1f %5.1f" % (C,F))

