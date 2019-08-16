# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 09:15:57 2018

@author: magge
"""

infile1 = open('Miniprojekt - Ankomsttider.txt', 'r')
infile1
ankomst_tid = []
for line in infile1:
    print(line)
    sekt = line.split()
    ankomst_tid.append(sekt[0])