# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:09:52 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

def rk4(f, t, x, h):
    k1 = f(t, x)
    k2 = f(t + 0.5*h, x + 0.5*h*k1)
    k3 = f(t + 0.5*h, x + 0.5*h*k2)
    k4 = f(t + h, x + h*k3)
    xr = x + h*(k1 + 2.0*(k2 + k3) + k4)/6.0
    return xr, t + h

t_in = 0
t_fin = 100
N = 1000
step = (t_fin - t_in)/float(N)

#alpha = 0.7
#beta = 0.001
#gamma = 0.3
#delta = 0.002

alpha = float(input("alpha:"))
beta = float(input("beta:"))
gamma = float(input("gamma:"))
delta = float(input("delta:"))

#x10 = 350
#x20 = 400

x1 = int(input("Initial-x:"))
y1 = int(input("Initial-y:"))

def function(t,x):
    return np.array([alpha*x[0] - beta*x[0]*x[1],
                     delta*x[0]*x[1] - gamma*x[1]])
    
X = np.zeros(N+1)
Y = np.zeros(N+1)

X[0] = x1
Y[0] = y1

t = 0.0

for k in range(N):
    Xr, t = rk4(function, t, np.array([X[k], Y[k]]), step)
    X[k+1] = Xr[0]
    Y[k+1] = Xr[1]

plt.plot(X,Y,'m',label="Model")
plt.plot([x1],[y1],'kd',label="Starting Point")
plt.title("Predator-prey Model")
plt.xlabel("Prey")
plt.ylabel("Predators")
plt.legend()