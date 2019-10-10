# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:20:42 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def mass_spring(k,m,c,x0,v0):
    """Function representing the mass-spring system with the use of different parameters"""
    #Lists for plotting the results
    pos_list = []
    vel_list = []
    acc_list = []
    pos_vel_err = []
    pos_acc_err = []
    vel_acc_err = []

    
    w0 = math.sqrt(k/m)
    zeta = c/(2*math.sqrt(m*k))
    
    def acceleration(x,dx):
        """Returns the second-order differential equation for motion of the dampened mass-spring system"""
        return -2*zeta*w0*dx - w0**2*x
    
    def pos_vel(t):
        """Generates the lists pos_list, vel_list and acc_list, with position, velocity and acceleration values for plotting"""
        x = x0
        dx = v0
        for time in range(len(t)):
            ddx = acceleration(x,dx)
            x += dx*t[time]
            dx += ddx*t[time]
            pos_vel_err.append(abs(x - dx))
            pos_acc_err.append(abs(x - ddx))
            vel_acc_err.append(abs(dx - ddx))
            pos_list.append(x)
            vel_list.append(dx)
            acc_list.append(ddx)
    
    t = np.linspace(0,10,10000)
    pos_vel(t)
    
    def system_plot():
        plt.plot(t[:350],pos_list[:350], 'm.',label="Posititon")
        plt.plot(t[:350],vel_list[:350], 'c.',label="Velocity")
        plt.plot(t[:350],acc_list[:350], 'g.',label="Acceleration")
        plt.grid()
        plt.legend()
    
    def error_system_plot():
        plt.plot(t[:350],pos_vel_err[:350], 'm.',label="Position-Velocity Error")
        plt.plot(t[:350],pos_acc_err[:350], 'c.',label="Position-Acceleration Error")
        plt.plot(t[:350],vel_acc_err[:350], 'g.',label="Velocity-Acceleration Error")
        plt.grid()
        plt.legend()
        
    def pick_plot():
        plot = str(input("Choose the plot:"))
        if plot == "system":
            system_plot()
        elif plot == "error":
            error_system_plot()
    pick_plot()
    
def pick():
    plot = str(input("Choose the system:"))
    if plot == "dampened":
        #Dampend system
        mass_spring(1.2,2.1,0.8,0.0,2.5)
    elif plot == "undampened":
        #Undampend system
        mass_spring(1.2,2.1,0.0,0.0,2.5)
    elif plot == "overdampened":
        #Overdampend system
        mass_spring(1.2,2.1,1.8,0.0,2.5)
pick()