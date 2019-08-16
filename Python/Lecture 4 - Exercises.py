# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:54:38 2018

@author: magge
"""

#2.2
Cdegrees = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for C in Cdegrees:
    C += 10
Cdegrees = list(range(0, 100, 10))
Fdegrees = [(9.0/5.0)*C+32 for C in Cdegrees]
print(Fdegrees)
for F in Fdegrees:
    F += 18.0
Capp = [(F-30)/2 for F in Fdegrees] #Capp for Capproximate
print(Capp)
#Ans: [1.0, 10.0, 19.0, 28.0, 37.0, 46.0, 55.0, 64.0, 73.0, 82.0]

#2.3
primes = [2, 3, 5, 7, 11, 13]
for P in primes:
    print("list elements:", P)
p = 17
primes.append(p)
print(primes)
#Ans:
#list elements: 2
#list elements: 3
#list elements: 5
#list elements: 7
#list elements: 11
#list elements: 13
#[2, 3, 5, 7, 11, 13, 17]

#2.8 right answer, rest are failed attempts
v0 = 15
g = 9.82
n = 20
t = (2*v0/g)/n

while t <= 2*v0/g:
    yt = v0*t-(1/2)*g*t**2
    t += (2*v0/g)/n
    print(yt)

n = 2
v0 = 24
g = 9.8
delta = ((2*v0)/g)/n

interval = range(0, n+1)
tid = [i/n * delta for i in interval]
funktion = [v0*t - 0.5*g*t**2 for t in tid]
for t, f in zip(tid, funktion):
    print("{:6.3f} {:6.3f}".format(t,f))

i = 0
def y(t): return (round(v0*t - 0.5*g*t**2, 4))
while i <= n:
    t = i/n * delta
    print(":{6.3f} {:6.3f}".format(t, y(t)))
    i += 1

n = 2
v0 = 24
g = 9.8
delta = ((2*v0)/g)/n

t = []
for idx in range(0, n+1):
    t.append(idx*delta)
#with for loop the table is [0.0, 2.4489795918367343, 4.897959183673469]

#2.9
v0 = 15
g = 9.82
n = 20
delta = (2*v0/g)/n

t = []
for idx in range(0, n+1):
    t.append(idx*delta)
    print(t)
y = [v0*T - 0.5*g*T**2 for T in t]
print(y)

for i in range(len(t)):
    print("%5.1f %5.1f" \
          % (t[i], y[i]))
#With the range construction the two lists are neatly
    #rounded to one decimal space.


#2.15
#a.
q = [['a','b','c'], ['d','e','f'], ['g','h']]
q[0][0] #a
q[1] #['d','e','f']
q[2][1] #h
q[-1][-2] #The result is g, because [-1] extracts the 
#third element in the list and [-2] extracts the second
#element in the list.

#b.
q[-1]
q[-2]
for i in q:
    for j in range(len(i)):
        print(i[j])