VarList1 = []
VarList2 = []
Varadd = []
Varsub = []
Varmul = []
Vardiv = []
Varmod = []
Varexpo = []

Vari = 0
Varj = 0

VarNum = int(input("Please enter the total number of element in list : "))
print("Please enter the values for First & Second List ")

while(Vari < VarNum):
 Varl1 = int(input("Please enter %d Element value of List1 : " %Varj))
 VarList1.append(Varl1)

 Varl2 = int(input("please enter %d Element value of List2 : " %Varj))
 VarList2.append(Varl2)

 Vari = Vari + 1

while(Varj < VarNum):
 Varadd.append(VarList1[Varj] + VarList2[Varj])
 Varsub.append(VarList1[Varj] - VarList2[Varj])
 Varmul.append(VarList1[Varj] * VarList2[Varj])
 Vardiv.append(VarList1[Varj] / VarList2[Varj])
 Varmod.append(VarList1[Varj] % VarList2[Varj])
 Varexpo.append(VarList1[Varj] ** VarList2[Varj])
 Varj = Varj + 1

print("List values after Addition = ", Varadd)
print("List values after Subtraction = ", Varsub)
print("List values after Multiplication = ", Varmul)
print("List values after Division = ", Vardiv)
print("List values after Modulus = ", Varmod)
print("List values after Exponent = ", Varexpo)