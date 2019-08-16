# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:59:28 2018

@author: magge
"""
import matplotlib.pyplot as plt

C = -10
dC = 2
C_list = []
F_list = []
while C <= 20:
    F = (9.0/5.0)*C + 32
    print(C,F)
    C = C + dC
    C_list.append(C)
    F_list.append(F)
    
plt.plot(C_list,F_list)
