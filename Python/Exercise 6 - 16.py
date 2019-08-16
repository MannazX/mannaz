# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:41:23 2018

@author: magge
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('---v0', type=float, default=0.0,
                    help='initial velocity', metavar='v0')

parser.add_argument('---mu', type=float, default=0.0,
                    help='initial velocity', metavar='mu')

parser.add_argument('---g', type=float, default=0.0,
                    help='initial velocity', metavar='g')

args = argparse.parse_args()

v0 = args.v0
mu = args.mu
g = args.g

d = 0.5*(v0**2)/(mu*g)

print("d({:.2f}) = {:.2f}".format(v0, d))

