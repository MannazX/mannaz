import numpy as np
anlist   = [1,2,1,2,1,3]
landlist = [2,1,4,2,3,1]
anlist   = np.array(anlist)
landlist = np.array(landlist)
ventetid = 0  
venteliste = []

# cumsum af lister
cum_landlist = np.cumsum(landlist)
cum_anlist = np.cumsum(anlist)

for i in range(len(landlist)):
    if i > 0:
        if cum_anlist[i] < cum_landlist[i-1]:
            ventetid = ventetid+ cum_landlist[i-1]-cum_anlist[i]
            venteliste.append(ventetid)
            ventetid = 0
        else:
            ventetid = ventetid
            venteliste.append(ventetid)
print(venteliste)


"""
Dette skulle gerne fungere!!!

Når vi er HELT færdige med koden kunne det være en ide at omskrive det til
samme type kode som vores anden for løkke, der laver de randomtider.
Altså sætte de to arrays sammen og bruge enumerate funktionen.

"""
"""
Ting der skal laves:
Lave de nye fly pr år, så de ligger inden for de rigtige intervaller, med de 
rigtige tidspunkter.

Fixe kø-flyene, så den ikke trækker 1 fra alle værdierne

Kø-system med 2 landingsbaner
"""