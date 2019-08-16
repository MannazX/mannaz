# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:15:12 2018

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt

def MCint(funktion, a, b, antal_punkter): #monte carlo integration formula
    x = np.random.uniform(a, b, antal_punkter)
    s = np.sum(funktion(x))
    I = (b-a)/antal_punkter*s
    return I

def en_funktion(x):
    return 2 + 3*x

a = 1
b = 2
antal_pkt = 1000000
MCint(en_funktion, a, b, antal_pkt)

værdier = np.empty(100)
punkt_antal = np.arange(antal_pkt // 100, antal_pkt + 1, antal_pkt // 100)
for indeks, test_punkter in enumerate(punkt_antal):
    værdier[indeks] = MCint(en_funktion, a, b, test_punkter)
_ = plt.plot(punkt_antal, værdier - 6.5)  # vi ved, at den rigtige værdi af integralet er 6.5
