"""
Created on Wed Oct 24 14:11:25 2018

@author: Frederik
"""
#importerer de nødvendige pakker. De 2 første er til selve opgaven og de 2 sidste er til animationen
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

"""
variablerne n, x og y skal være globale variabler, ellers har animationen
ikke nogen x og y værdier at gå efter, så den laver bare en masse random punkter
istedet. 
"""

n = 5000000                       # Bestemmer antallet af punkter
r = 1                             # grænserne for x og y, samt radius af cirklen
x = np.random.uniform(-r, r, n)   # laver n forskellige x-værdier fra -r til r
y = np.random.uniform(-r, r, n)   # laver n forskellige y-værdier fra -r til r


def G(n, r):                                                                   # Definerer funktionen, som udregner den approksimerede pi
    m = np.sum(np.square(x)+np.square(y) < r)                                  # Tjekker x og y igennem for x^2 + y^2 < 1
    areal = m / n * (2*r)**2                                                   # Udregner forholdet mellem cirklens areal og firkantens areal
    approx_pi = areal / r                                                      # Udregner den approksimerede pi
    return approx_pi

print("Den approksimerede pi:", G(n, r))                                       # Printer approximate pi
print("Den rigtige pi:", math.pi)                                              # Printer rigtige pi
print("Afvigelse:", abs(math.pi-G(n, r)))                                      # Printer Afvigelsen

# Nedenstående er ekstra, som laver en figur med cirkel og punkter:

fig = plt.figure()                                                             # Laver figur
plt.xlim(-r-0.01, r+0.01)                                                      # Afgrænser vinduet fra x=-r-0,01 til x=r+0,01 på x-aksen (+-0,01 for hele cirklen vises) 
plt.ylim(-r-0.01, r+0.01)                                                      # Det samme som ovenstående, men for y
graph, = plt.plot([], [], 'o', alpha = 0.5)                                    #Tomt plot, som skal fyldes op med punkter, der er halvt gennemsigtige
circle1 = plt.Circle((0, 0), r ,linewidth=4.0 , color='r', fill = False)       # Laver rød cirkel med en omkreds der er 4 bred
ax = fig.gca()                                                                 # fig.gca kalder den aktive figur
ax.add_artist(circle1)                                                         # Tilføjer cirkel til den aktive figur

def animate(i):                                                                # Defiinerer animationen 
    graph.set_data(x[:i+1], y[:i+1])                                           # Plotter data fra x[0:i+1] og y[0:i+1] 
    return graph

ani = FuncAnimation(fig, animate ,interval = 1)                                # Interval i ms, som plotter punkterne
plt.show()                                                                     # Viser plottet
