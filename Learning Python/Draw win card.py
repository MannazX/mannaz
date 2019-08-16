# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:40:44 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
import random

def win_draw():
    cards = ["one","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]
    my_draws = []
    computer_draws = []
    win_card = random.choice(cards)
    for i in range(25):
        draw = random.choice(cards)
        my_draws.append(draw)
    for i in range(25):
        draw = random.choice(cards)
        computer_draws.append(draw)
    for i in range(25):
        if my_draws[i] == win_card:
            print("You win! you drew the win card")
            break
        elif computer_draws[i] == win_card:
            print("Computer wins! it drew the win card")
            break
    #print(my_draws)
    #print(computer_draws)
    print(win_card)

N = int(input("Iterations ="))
for i in range(N):
    win_draw()