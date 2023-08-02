def funcadd(Varx, Vary):
    return Varx + Vary

def funcsub(Varx, Vary):
    return Varx - Vary

def funcmul(Varx, Vary):
    return Varx * Vary

def funcdiv(Varx, Vary):
    return Varx / Vary

print("Please select the operation:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")  

while True:
    Varch = input("Enter your choice (1/2/3/4):")

    if Varch in ('1', '2', '3', '4'):
        Varno1 = float(input("Enter first number:"))
        Varno2 = float(input("Enter second number:"))

        if Varch == '1':
            print(Varno1, '+', Varno2, '=', funcadd(Varno1, Varno2))
        elif Varch == '2':
            print(Varno1, '-', Varno2, '=', funcsub(Varno1, Varno2))
        elif Varch == '3':
            print(Varno1, '*', Varno2, '=', funcmul(Varno1, Varno2))
        elif Varch == '4':
            if Varno2 != 0:  
                print(Varno1, '/', Varno2, '=', funcdiv(Varno1, Varno2))
            else:
                print("Error: Division by zero is not allowed.")
        break  
    else:
        print("Invalid input!")
