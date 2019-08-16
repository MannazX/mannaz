# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:54:06 2018

@author: magge
"""

stars = ['Alpha Centauri A', 'Alpha Centauri B', 'Alpha Centauri C', 'Bernards Star', 'Wolf 359', 'BD +36 degrees 2147', 'Luyten 726-8 A', 'Luyten 726-8 B', 'Sirius A', 'Sirius B', 'Ross 154']

stars = {'Alpha Centauri A': 1.56, 'Alpha Centauri B': 0.45, 'Alpha Centauri C':0.00006, 'Bernards Star': 0.0005, 'Wolf 359': 0.00002, 'BD +36 degrees 2147': 0.006, 'Luyten 726-8 A':0.00006, 'Luyten 726-8 B': 0.00004, 'Sirius A': 23.6, 'Sirius B': 0.003, 'Ross 154': 0.0005} 
stars
for lum in stars:
    print(lum)
    print(stars[lum])


