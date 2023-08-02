Vari = int(input("Enter the number from which you want to start adding numbers: "))
Varnum = int(input("Enter the number till which you want to add all numbers: "))
Varsum = 0
Vart = Vari
while Vari <= Varnum:
 Varsum = Varsum+Vari
 Vari=Vari+1

print("The Sum of number from ",Vart,"till ",Varnum,"is = ", Varsum)