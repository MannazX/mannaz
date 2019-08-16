# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:20:00 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
from matplotlib.animation import FuncAnimation

xw = []
yw = []
np.random.seed(92)
def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = np.random.choice(['N','S','E','W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        elif step == 'W':
            x = x - 1
        xw.append(x)
        yw.append(y)
    return (x,y)

for i in range(25):
    walk = random_walk(25)
    print(walk, "The distance from starting point is:",
          abs(walk[0]) + abs(walk[1]))

fig = plt.figure()
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.grid(linewidth=1,alpha=0.5)
graph, = plt.plot([],[],'ks',alpha=0.3)

def animate(i):
    graph.set_data(xw[:i+1],yw[:i+1])
    return graph

ani = FuncAnimation(fig, animate, interval=10, repeat=False)
plt.show()
#plt.plot(xw,yw,'ks-',alpha=0.3)
