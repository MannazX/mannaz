import numpy as np
anlist   = [0,1,3,1,1,4,1]
landlist = [2,3,4,1,1,1,1]
anlist   = np.array(anlist)
landlist = np.array(landlist)
ventetid = 0  
#venteliste = []

# cumsum af lister
cum_landlist = np.cumsum(landlist)
cum_anlist = np.cumsum(anlist)

for i in range(len(landlist)):
    if i > 0:
        if cum_anlist[i] < cum_landlist[i-1]:
            ventetid = ventetid+ cum_landlist[i-1]-cum_anlist[i]
#            venteliste.append(ventetid)
#            ventetid = 0
        else:
            ventetid = ventetid
print(ventetid)


"""
Dette skulle gerne fungere!!!

Når vi er HELT færdige med koden kunne det være en ide at omskrive det til
samme type kode som vores anden for løkke, der laver de randomtider.
Altså sætte de to arrays sammen og bruge enumerate funktionen.

"""