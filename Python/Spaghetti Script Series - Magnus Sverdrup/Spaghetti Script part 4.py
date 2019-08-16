# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math as m

def slope(a,b,c,x):
    dy = a*x+(b+c)
    return dy

def Solved_Eq(a,b,c,n,h,r):
    y_list = []
    x_list = []
    p_list = []
    y = 0
    x = 0
    for x in range(n):
        y_list.append(y)
        x_list.append(x)
        y += h*slope(a,b,c,x)
        p = c*m.exp(a*x-b)
        p_list.append(p)
        x += h
    plt.subplot(1,2,1)
    plt.plot(x_list,y_list,'r',linestyle = 'dashed')
    if r == 1:
        plt.subplot(1,2,2)
        plt.plot(x_list,p_list,'m',linestyle = 'dashed')
        
Solved_Eq(2,10,20,20,1,1)        
Solved_Eq(2,10,20,20,10,1)
Solved_Eq(2,10,20,20,25,1)         