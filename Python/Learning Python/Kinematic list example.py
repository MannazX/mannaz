# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 11:04:30 2018

@author: magge
"""
import matplotlib.pyplot as plt

def Projectile(n,v1,a):
    d = []
    t = []
    t_indx = range(n+1)
    d_indx = 0

    for i in t_indx:
        t.append(i)
        d_indx += v1*i + 0.5*a*i**2
        d.append(d_indx)
    
    print(t)
    print(d)
    
    plt.plot(t, d, 'ro')
    plt.xlabel('Time (s)'); plt.ylabel('Distance (m)')
    plt.title('Plot of distance over time of projectile')

Projectile(20,22,-9.81)