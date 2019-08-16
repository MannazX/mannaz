# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:11:40 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy import fft
import scipy

N = 100

def fun_sin(t,w):
    return np.sin(w*t)

def fun_cos(t,w):
    return np.cos(w*t)

def error(t,w):
    return abs(np.sin(w*t)-np.cos(w*t))

#t = np.linspace(-2*np.pi,2*np.pi,1000)
t = np.linspace(0,2*np.pi,1000)

w = 0
for k in range(N):
    w += k**2   
    f = fun_sin(t,w)
    ff = fft(f)
    g = fun_cos(t,w)
    fg = fft(g)
    e = error(t,w)
    fe = fft(e)
    plt.plot(t,ff,'b')
    plt.title("Plot of Fourier Transformed Sine Wave")
    plt.xlabel("Period [rad]"); plt.ylabel("Amplitude")
#    plt.plot(t,fg,'c')
#    plt.title("Plot of Fourier Transformed Cosine Wave")
#    plt.xlabel("Period [rad]"); plt.ylabel("Amplitude")
#    plt.ylim(-150,510)
#    plt.plot(t,fe,'m.',alpha=0.3)
#    plt.ylim(-250,250)
#    plt.title("Error plot of the Two Periodic Functions")
#    plt.xlabel("Period [rad]"); plt.ylabel("Amplitude")