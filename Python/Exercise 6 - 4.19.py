# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:51:11 2018

@author: magge
"""
import sys

try:
    C = float(sys.arg[1])
except:
    print('C must be provided as command-line argument')
    sys.exit(1)
    #sys.arg[1] is an illegal indexing - no command-line
    #arguments provided
    
    #content of string sys.arg[1] is not a number that can
    #just be converted into a float

try:
    C = float(sys.argv[1])
except IndexError:
    print('Celcius degrees must be supplied on the command line')
    sys.exit(1)
except ValueError:
    print('Celcius degrees must be a pure number, '\
          'not "%s"' % sys.argv[1])
    sys.exit(1)
    
F = 9.0*C/5 + 32
print('%gC is %.1fF' % (C,F))


