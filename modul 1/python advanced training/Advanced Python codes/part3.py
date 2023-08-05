class clssub:
 def funcf1(self,str1):
  return self.funcf2([], sorted(str1))

 def funcf2(self, curr, str1):
  if str1:
    return self.funcf2(curr, str1[1:]) + self.funcf2(curr+[str1[0]], str1[1:])
  return [curr]
a1=[]
varn=int(input("Enter no of elements of list:"))
for i1 in range(0, varn):
 varb=int(input("Enter element:"))
 a1.append(varb)
print("Printing Subsets:")
print(clssub().funcf1(a1))