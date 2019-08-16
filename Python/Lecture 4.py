# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:20:36 2018

@author: magge
"""

C = -20
dC = 5
while C <= 40:
    F = (9.0/5.0)*C + 32
    print(C, F)
    C = C + dC
    
#Initial conditions: C = -20, dC = 5
#while keyword. Condition: C <= 40

#Boolean: Either true or false
C = 25
C <= 40
C <= 20

#Expressions
C == 40
C != 40
C >= 40
C > 40
C < 40

#Logical and, or, not
x < 1 and y > 2

a = 1
n = 13
while a <= n:
    if a % 2:
        print(a)
    a += 1

#For even numbers type if not a. 
a = 1
n = 13
while a <= n:
    if not a % 2:
        print(a)
    a += 1

#List operations
C = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25] 
C.append([45, 50])

C = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25] 
C = C + [45, 50]

C = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25] 
del C[0]

print(C)

#store odd numbers in a list 
C = [ ]
C.append([1,3,5])
print(C)

degrees = [0, 10, 20, 30, 40, 100]
for C in degrees:
    print("list element:", C)
print("The degree list has %d elements" % (len(degrees)))

for element in some_list:
    <process element>
    
index = 0
while index < len(some_list):
    element = some_list[index]
    <process element>
    index += 1

for C in Cdegrees:
    C += 5
Cdegrees = list(range(-20, 45, 5))
for i, C in enumerate(Cdegrees):
    Cdegrees[i] = C + 5
print(Cdegrees)

newlist = [f(e) for e in oldlist]
Cdegrees = [-10 + 2.5*i for i in range(0,21)] 
Fdegrees = [(9.0/5.0)*C + 32 for C in Cdegrees]

Cdegrees = []
for i in range(0, 21)
    C = -20 + 2.5*i
    Cdegrees.append(C)
    
a = [n for n in range(1, n + 1, 2) if n % 2]
print(a)
    
#The general format is mylist[start:stop]
A = [2.0, 3.0, 8.0, 10.0]
A[0:3] # [2.0, 3.0, 8.0]
A[2:3] # [8.0]
A[3:-1] # []
A[2:] # [8.0, 10.0]
A[:3] # [2.0, 3.0, 8.0]

liste = [1,2,3,4]
liste[-1:4]

Cdegrees = list(range(-20,45,5))
Fdegrees = [(9.0/5.0)*C+32 for C in Cdegrees]
tab1 = [Cdegrees, Fdegrees]
tab2 = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
tab3 = zip(Cdegrees, Fdegrees)
print(tab1)
print(tab2)
print(tab3)
for i in range(len(Cdegrees)):
    print("%5.1f %5.1f" \
          % (Cdegrees[i], Fdegrees[i]))

scores = []
scores.append([12, 16, 11, 12])
scores.append([9])
scores.append([6, 9, 11, 14, 17, 15])
for player in scores:
    for game in player:
        print("%4d" % game),
    print("")
    
for p in range(len(scores)):
    for g in range(len(scores[p])):
        score = scores[p][g]
        print("%4d" % score),
    print("")
        
        
t = (1, 4, 5)
t[:2]
t = t + (6, 8)
6 in t
