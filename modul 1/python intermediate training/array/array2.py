def func_insertion(Vararr):
 Varn = len(Vararr)
 for j in range(1, Varn):
  Varkey = Vararr[j]
  i = j-1
  while i >= 0 and Varkey < Vararr[i]:
   Vararr[i+1] = Vararr[i]
   i -= 1
  Vararr[i+1] = Varkey
 return Vararr

Vararr = [45,2,34,12,67,89,304,45,3]
print("Sorted array: ")
print(func_insertion(Vararr))
