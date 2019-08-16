import numpy as np

"""
nedsætte = 1 # skal laves til K=K0*(1-r)^n hvor K0=1 r=5% og n er antal år
stigning = 1 # skal laves til K=K0*(1+r)^n hvor K0=1 r=5% og n er antal år
"""
# Laver random ankomsttider 

an_arr = np.loadtxt("Miniprojekt - Ankomsttider.txt", delimiter = ",")
an_arr = np.asarray(an_arr,np.int)
an_multiarr = []

for row, line in enumerate(an_arr):
        h = np.random.randint(an_arr[row,0],an_arr[row,1],an_arr[row,2])
        an_multiarr.append(h)
random_an_tid = np.concatenate(an_multiarr)
np.random.shuffle(random_an_tid)
print("Tilfældige ankomsttider:","\n" ,random_an_tid)


"""
Til docstring:
    
Packages:
    Numpy pakken benyttes og omkaldes til "np".

Variabler: 
    an_arr = loader tekstfilen "ankomsttider" og konverterer "," til ny linje 
    i et array.
    
    an_multiarr = Et array, som indeholder antal fly-ankomsttider arrays.
    
    random_an_tid = Samler an_multiarr til et stort array, som bliver blandet 
    med random.shuffle funktionen..
"""