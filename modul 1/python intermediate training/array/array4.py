def func_linearsrc(Vararr, Varnum):
 Varpos = -1
 for idx in range(0, len(Vararr)):
  if Vararr[idx] == Varnum:
   Varpos = idx
   break
 return(Varpos)

Vararr = [10,2,345,56,789,67,46,45,34,56,78,8967,56]
Varnum = 78
Varf = func_linearsrc(Vararr, Varnum)
if Varf != -1:
 print('The number %d is found at a position of %d' %(Varnum, Varf+1))
else:
 print('Number is not found in the given array')
