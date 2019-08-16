# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:29:10 2018

@author: magge
"""
import numpy as np


infile = open('Data for learning python.txt', 'r')

lines = []
for line in infile:
    print(line)
    lines.append(line)
    
print(lines)
 
infile.close()

infile = open('Data for learning python.txt', 'r')
filestr = infile.read()
N = filestr.split()
N

N_list = []
for t in N:
    print(t)
    N_list.append(t)
print(N_list)

N_list = np.array(N_list)
for i in range(len(N_list)):
    if N_list[i] < N_list[i-1]:
        print(0)
    else:
        break

