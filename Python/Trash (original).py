import numpy as np
anlist   = [1,2,1,2,1,3]
landlist = [2,1,4,2,3,1]
anlist   = np.array(anlist)
landlist = np.array(landlist)
ventetid = 0

# cumsum af lister
cum_landlist = np.cumsum(landlist)
cum_anlist = np.cumsum(anlist)
print(cum_anlist,"\n",cum_landlist)
p = 0
for i in range(len(cum_anlist)):
    if i < 1:
        if cum_anlist[i] >= 0:
            ventetid = 0
    if i > 1:
        if cum_anlist[i] >= cum_landlist[i-1]:
            ventetid = 0
        else:
            ventetid = ventetid + cum_landlist[i-1]-cum_anlist[i]
print(ventetid)
