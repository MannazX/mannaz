# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:04:15 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
from matplotlib.animation import FuncAnimation


x = np.linspace(0,10,20)
y = np.arange(1,100,5)
yl = [1]
xl = [0]

yl = np.asarray(yl)
yl = np.append(yl,y)
xl = np.asarray(xl)
xl = np.append(xl,x)

fig = plt.figure()
plt.xlim(0,10)
plt.ylim(0,100)
graph, = plt.plot([],[],'ro-')
graph2, = plt.plot([],[],'wo-')

def animate(i):
    graph.set_data(xl[len(xl)-i:len(xl)],yl[len(yl)-i:len(yl)])
    graph2.set_data(x[:i+1],y[:i+1])
    return graph, graph2

ani = FuncAnimation(fig, animate, interval = 1000)
plt.show()
