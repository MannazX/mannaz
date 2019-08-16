# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:13:10 2018

@author: magge
"""
from math import sqrt
def roots(a, b, c):
    """
    The roots are ....
    
    example
    >>> roots(-2.0, 4.0, 5.0)
    (3.4833147735478827, -11.483314773547882)
    
    """
    
    posr = -b + sqrt(b**2 - 4*a*c)
    negr = -b - sqrt(b**2 - 4*a*c)
    return posr, negr
print(roots(-2.0, 4.0, 5.0))

import doctest
doctest.testmod()