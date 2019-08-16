# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:58:12 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
import random

def draw(N):
    cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
    options = [i for i in cards]
    your_draws = []
    bot_draws = []
    your_score = 0
    bot_score = 0
    for i in range(N):
        your_draw = random.choice(options)
        your_draw_rank = 0
        bot_draw_rank = 0
        bot_draw = random.choice(options)
        for i in cards:
            if your_draw == i:
                your_draw_rank += cards[i]
            if bot_draw == i:
                bot_draw_rank += cards[i]
        if your_draw_rank > bot_draw_rank:
            your_score += 1
        elif bot_draw_rank > your_draw_rank:
            bot_score += 1
        your_draws.append(your_draw)
        bot_draws.append(bot_draw)
    print("Your draws:",your_draws)
    print("Bot draws:",bot_draws)
    print("Your score: {:}".format(your_score))
    print("Bot score: {:}".format(bot_score))

N = int(input("Number of rounds:"))
draw(N)