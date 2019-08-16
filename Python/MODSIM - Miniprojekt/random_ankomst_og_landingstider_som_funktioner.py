import numpy as np

def tilfældig_ankomst_og_landingstider(stigning = 0.05, år = 0):
    """
    Docstring:
    
    Packages:
    Numpy pakken benyttes og omkaldes til "np".

    Variabler: 
    an_arr = loader tekstfilen "ankomsttider" og konverterer "," til ny linje 
    i et array.
    
    an_multiarr = Et array, som indeholder antal fly-ankomsttider arrays.
    
    random_an_tid = Samler an_multiarr til et stort array, som bliver blandet 
    med random.shuffle funktionen..
    
    """
    an_arr = np.loadtxt("Miniprojekt - Ankomsttider.txt", delimiter = ",")
    an_arr = np.asarray(an_arr,np.int)
    an_multiarr = []

    land_arr = np.loadtxt("Miniprojekt - Landingstider.txt", delimiter = ",")
    land_arr = np.asarray(land_arr,np.int)
    land_multiarr = []

    for row, line in enumerate(an_arr):
        h = np.random.randint(an_arr[row,0]*(1-stigning)**år,
                              an_arr[row,1]*(1-stigning)**år,
                              an_arr[row,2])
        an_multiarr.append(h)
    
    for row, line in enumerate(land_arr):
        h = np.random.randint(land_arr[row,0]*(1-stigning)**år,
                              land_arr[row,1]*(1-stigning)**år,
                              land_arr[row,2])
        land_multiarr.append(h)
    
    random_an_tid = np.concatenate(an_multiarr)
    np.random.shuffle(random_an_tid)
    
    random_land_tid = np.concatenate(land_multiarr)
    np.random.shuffle(random_land_tid)
    return (print("Tilfældige ankomsttider", "\n",random_an_tid),
            print("Tilfældige landingstider", "\n",random_land_tid))