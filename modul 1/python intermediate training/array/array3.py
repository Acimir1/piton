def func_selection(Vararr):
 Varn = len(Vararr)
 for j in range(Varn):
  Varindex = j
  for i in range(j+1, Varn):
   if Vararr[Varindex] > Vararr[i]:
    Varindex = i
  if j != Varindex:
   Vartemp = Vararr[j]
   Vararr[j] = Vararr[Varindex]
   Vararr[Varindex] = Vartemp
 return Vararr

Vararr = [34,2,45,57,34,56,20,102]
print("Sorted array: ")
print(func_selection(Vararr))