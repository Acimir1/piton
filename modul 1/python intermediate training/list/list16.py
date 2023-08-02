VarList1 = [100, 200, 300, 400]
VarList2 = [4, 6, 8, 10]

Varadd=[]
Varsub=[]
Varmul=[]
Vardiv=[]
Varmod=[]
Varexpo=[]

for varj in range(4):
 Varadd.append(VarList1[varj] + VarList2[varj])
 Varsub.append(VarList1[varj] - VarList2[varj])
 Varmul.append(VarList1[varj] * VarList2[varj])
 Vardiv.append(VarList1[varj] / VarList2[varj])
 Varmod.append(VarList1[varj] % VarList2[varj])
 Varexpo.append(VarList1[varj] ** VarList2[varj])

print("The Values of List after Addition = ", Varadd)
print("The Values of List after Subtraction = ", Varsub)
print("The Values of List after Multiplication = ",Varmul)
print("The Values of List after Division = ", Vardiv)
print("The Values of List after Modulus = ", Varmod)
print("The Values of List after Exponent = ", Varexpo)