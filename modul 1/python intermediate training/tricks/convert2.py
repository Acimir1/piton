Varlist=[("Ashok", 84),("Pooja", 34),("Neena", 56),("Ritesh", 88),("Shraddha", 80),("Nitin", 78)]
Vardict=dict()

for i,j in Varlist:
 Vardict.setdefault(i, []).append(j)
print(Vardict)