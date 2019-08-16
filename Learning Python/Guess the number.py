# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:10:55 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
import random

# Time to guess the number
print("Place your best guess in the console!")

number = random.randint(1,100)
attempt = 0
guess = 0
while guess != number:
    guess = int(input("Your guess is:"))
    if guess == number:
        attempt += 1
        print("You guessed the number!")
        print("You used {:} guesses".format(attempt))
        break
    elif guess > number:
        attempt += 1
        print("Your guess is above the number, re-guess!")
    elif guess < number:
        attempt += 1
        print("Your guess is below the number, re-guess!")


