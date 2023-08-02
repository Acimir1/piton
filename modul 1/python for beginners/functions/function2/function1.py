def calc_lcm(Varx, Vary):
    if Varx > Vary:
        Varg = Varx
    else:
        Varg = Vary

    while True:
        if (Varg % Varx == 0) and (Varg % Vary == 0):
            VarLCM = Varg
            break
        Varg += 1

    return VarLCM

Varno1 = int(input("Enter first number: "))
Varno2 = int(input("Enter second number: "))

print("The L.C.M. is: ", calc_lcm(Varno1,Varno2))