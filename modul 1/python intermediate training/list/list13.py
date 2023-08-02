VarList1=[]
VarList2=[]
VarTotal=[]

VarNum = int(input("Please enter the Total Number of List elements you want"))
print("Please enter the values of the First List ")
for j1 in range(1, VarNum + 1):
 Varval = int(input("Please enter the Value of %d Element : " %j1))
 VarList1.append(Varval)

print("Please enter the values of the Second List ")
for j2 in range(1, VarNum + 1):
 Varval = int(input("Please enter the Value for %d Element : " %j1))
 VarList2.append(Varval)

for j3 in range(VarNum):
 VarTotal.append(VarList1[j3] + VarList2[j3])

print("The Sum of both the list is : ", VarTotal)