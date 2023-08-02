def calc_hcf(Varx,Vary):
    if Varx>Vary:
        Vars = Vary
    else:
        Vars = Varx
    for j in range(1,Vars+1):
        if ((Varx % j == 0) and (Vary % j == 0)):
            VarHCF = j
        return VarHCF
    
Varno1 = int(input("Enter first number: "))
Varno2 = int(input("Enter second number: "))

print("The H.C.F. is: ", calc_hcf(Varno1,Varno2))
