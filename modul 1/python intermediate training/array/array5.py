def func_binarysrc(Vararr, Varnum):
 Vars = 0
 Vare = len(Vararr)
 Varm = (Vars + Vare ) // 2
 Varf = False
 Varp = -1
 while Vars <= Vare:
  if(Vararr[Varm] == Varnum):
   Varf = True
   Varp = Varm
   break
  if Varnum > Vararr[Varm]:
   Vars = Varm + 1
   Varm = (Vars + Vare) // 2
  else:
   Vare = Varm - 1
   Varm = (Vars + Vare) // 2
 return(Varf, Varp)

Vararr=[0,12,14,15,16,17,18,20,30,50]
Varnum = 16
Varf = func_binarysrc(Vararr, Varnum)
if Varf[0]:
 print('Number %d is found in the array at %d Position: ' %(Varnum, Varf[1]+1))
else:
 print('Number not found in the array')