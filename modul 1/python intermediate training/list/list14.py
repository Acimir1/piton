VarList1=[]
VarList2=[]
VarTotal=[]

VarNum = int(input("Please enter the total number of elements you want in list :"))
print("Please enter the Value of First & Second List ")
for j1 in range(1, VarNum + 1):
 Varl1 = int(input("Please enter the %d Element Value of List1 : " %j1))
 VarList1.append(Varl1)

 Varl2 = int(input("Please enter the %d Element Value of List2 : " %j1))
 VarList2.append(Varl2)

for j1 in range(VarNum):
 VarTotal.append(VarList1[j1] + VarList2[j1])

print("The sum of two list is : ", VarTotal)