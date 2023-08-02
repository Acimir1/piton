VarList1 = []
VarList2 = []
Varadd = []
Varsub = []
Varmul = []
Vardiv = []
Varmod = []
Varexpo = []

VarNum = int(input("Please enter the total number of element in list : "))
for varj in range(1, VarNum + 1):
 Varl1 = int(input("Please enter %d Element value of List1 : " %varj))
 VarList1.append(Varl1)

 Varl2 = int(input("please enter %d Element value of List2 : " %varj))
 VarList2.append(Varl2)

for varj in range(VarNum):
 Varadd.append(VarList1[varj] + VarList2[varj])
 Varsub.append(VarList1[varj] - VarList2[varj])
 Varmul.append(VarList1[varj] * VarList2[varj])
 Vardiv.append(VarList1[varj] / VarList2[varj])
 Varmod.append(VarList1[varj] % VarList2[varj])
 Varexpo.append(VarList1[varj] ** VarList2[varj])

print("List values after Addition = ", Varadd)
print("List values after Subtraction = ", Varsub)
print("List values after Multiplication = ", Varmul)
print("List values after Division = ", Vardiv)
print("List values after Modulus = ", Varmod)
print("List values after Exponent = ", Varexpo)