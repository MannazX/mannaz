# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:58:18 2018

@author: magge
"""
import random
import numpy as np

coinflip = np.random.randint(0, 2, size=100) #generates random integar - probability of heads or tails
antal_tails = np.sum(np.logical_not(coinflip)) #generates probability of flipping tails (probability of not flipping heads)
antal_tails #probability of tails

#tails -0 and heads -1
#not makes 1's to 0's and vice versa