def Convertfunc(Vartup, Vardict):
 for i,j in Vartup:
  Vardict.setdefault(i, []).append(j)
 return Vardict


Vartup = [("John", 20),("Leena",23),("Meena",45),("Johnson",46),("Peter",67),("Stc",34)]
Vardict={}
print(Convertfunc(Vartup,Vardict))