# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:12:51 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy import fft

N = 100

def error(t,w):
    return abs(np.sin(w*t)-np.cos(w*t))

#t = np.linspace(-2*np.pi,2*np.pi,1000)
t = np.linspace(0,2*np.pi,1000)

w = 0
for k in range(N):
    w += k**2
    e = error(t,w)
    fe = fft(e)
    plt.plot(t,fe,'m.',alpha=0.3)
    plt.ylim(-250,250)
    plt.title("Error plot of the Two Periodic Functions")
    plt.xlabel("Period [rad]"); plt.ylabel("Amplitude")
    