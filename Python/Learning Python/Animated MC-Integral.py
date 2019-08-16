# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:31:09 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
#import math as m
from matplotlib.animation import FuncAnimation

np.random.seed(82)
n = 5000000
a = 1
b = 5
m = 148.8
x = np.random.uniform(a,b,n)
y = np.random.uniform(0,m,n)
    
def MCint_area(f,a,b,m,n):
    n_under = y[y<f(x)].size
    area = n_under/n*m*(b-a)
    return area

def exp(t):
    return np.exp(t)

print("The area under the curve exp is {:.2f}".format(MCint_area(exp,a,b,m,n)))

fig = plt.figure()
plt.xlim(a,b)
plt.ylim(0,m)
graph, = plt.plot([],[],'gx',alpha=0.5)

def animate(i):
    graph.set_data(x[:i*100+1],y[:i*100+1])
    return graph

ani = FuncAnimation(fig, animate, None, blit=False, interval=0.0000001)
plt.show()

t = np.linspace(1,5,n)
exp = exp(t)
print("Each point that happens to land under the graph approximates its area.")

plt.plot(t,exp,'m')
plt.title("Monte Carlo Integral Approximation of Exponential Graph")
plt.xlabel("x-values"), plt.ylabel("y-values")