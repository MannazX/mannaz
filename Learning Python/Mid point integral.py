# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:38:51 2018

@author: magge
"""

def Mid_p_int(f,a,b,n):
    h = (b-a)/n
    sum1 = 0
    for i in range(0,n-1):
        sum1 += f(a+i*h+(1/2)*h)
    return h*sum1

print(Mid_p_int(lambda x:x,2,3,100))
    