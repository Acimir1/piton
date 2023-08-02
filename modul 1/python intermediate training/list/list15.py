VarList1 = []
VarList2 = []
VarTotal = []
vari = 1
varj = 0
VarNum = int(input("Please enter the Total Number of List Element you want"))
print("Please enter the items of First & Second List ")
while(vari <= VarNum):
 Varl1 = int(input("Value of %d Element of List1 : " %vari))
 VarList1.append(Varl1)

 Varl2 = int(input("Value of %d Element of List2 : " %vari))
 VarList2.append(Varl2)

 vari = vari+1

while(varj < VarNum):
 VarTotal.append(VarList1[varj] + VarList2[varj])
 varj=varj+1

print("The Sum of two list is: ", VarTotal)