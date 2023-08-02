def func_bubble(Vararr):
 Varn = len(Vararr)
 for j in range(Varn):
  for i in range(0, Varn-j-1):
   if Vararr[i] > Vararr[i+1]:
    Vartemp = Vararr[i]
    Vararr[i] = Vararr[i+1]
    Vararr[i+1] = Vartemp
 return Vararr

Vararr=[2,4,5,7,8,19,59,12,24,455]
print("Sorted Array: ")
print(func_bubble(Vararr))
