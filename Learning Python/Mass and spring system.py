# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:58:17 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math

print("Welcome user, get ready for the time of your life!")

#Physical constant parameters
k = 1.2
m = 2.1
c = 0.8

w0 = math.sqrt(k/m)
zeta = c/(2*math.sqrt(m*k))

#Initial conditions
x0 = 0.0
v0 = 2.5

#Lists for plotting the results
pos_list = []
vel_list = []
acc_list = []

def acceleration(x,dx):
    """Returns the second-order differential equation for motion of the dampened mass-spring system"""
    return -2*zeta*w0*dx - w0**2*x

def pos_vel(t):
    """Generates the lists pos_list and vel_list, with position and velocity values for plotting"""
    x = x0
    dx = v0
    for time in range(len(t)):
        ddx = acceleration(x,dx)
        x += dx*t[time]
        dx += ddx*t[time]
        pos_list.append(x)
        vel_list.append(dx)
        acc_list.append(ddx)

t = np.linspace(0,5,5000)
pos_vel(t)

plt.plot(t[:350],pos_list[:350], 'm',label="Posititon")
plt.plot(t[:350],vel_list[:350], 'c',label="Velocity")
plt.plot(t[:350],acc_list[:350], 'g',label="Acceleration")
plt.grid()
plt.legend()
