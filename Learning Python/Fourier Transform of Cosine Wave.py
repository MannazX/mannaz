# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:09:53 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy import fft

N = 100

def fun_cos(t,w):
    return np.cos(w*t)

t = np.linspace(-2*np.pi,2*np.pi,1000)
#t = np.linspace(0,2*np.pi,1000)

w = 0
for k in range(N):
    w += k**2
    g = fun_cos(t,w)
    fg = fft(g)
    plt.plot(t,fg,'c')
    plt.title("Plot of Fourier Transformed Cosine Wave")
    plt.xlabel("Period [rad]"); plt.ylabel("Amplitude")
    plt.ylim(-150,510)