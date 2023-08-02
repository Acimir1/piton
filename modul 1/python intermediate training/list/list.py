a=[]
Varn=int(input("Enter the no of values in the list:"))
for i in range(0, Varn):
 Varele = input("Enter the Value " +str(i+1) + ":")
 a.append(Varele)
Varmax = len(a[0])
Vartemp=a[0]
for j in a:
 if(len(j)>Varmax):
  Varmax=len(j)
  Vartemp=j
print("The largest word from the list is:", Vartemp)