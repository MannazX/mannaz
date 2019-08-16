# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:15:36 2018

@author: bergl

#opgave 2.9
"""
v0=2            #start hastighed i [m/s]
g=9.81          #tyngdeaccelrationen i [m/s^2]
n=10            #antallet af jævnt fordelte steps
dt=2*v0/g/(n-1) #"længden" af hvert step i [s]

listt=[]
listy=[]
for i in range(0,n):
    t=i*dt
    listt.append(t)
    y=v0*t-0.5*g*t**2
    listy.append(y)
    
print(listy,"\n")
print(listt)

from matplotlib.pyplot import plot,show
plot(listt,listy,"ro")
show()



