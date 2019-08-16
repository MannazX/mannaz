# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:28:29 2018

@author: magge
"""
import sys

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