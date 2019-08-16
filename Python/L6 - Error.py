# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 09:30:17 2018

@author: magge
"""

import sys

if len(sys.argv) != 2:
    print("Please provide one Celcius degree value as input on the \
          command line.")
    sys.exit(1)

C = float(sys.argv[1])
F = (9.0/5)*C + 32
print("{:.2f} degree Celcius is {:.2f} degree Fahrenheit".format(
        C, F))

