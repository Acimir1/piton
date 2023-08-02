Varrows = int(input("Enter the number of rows: "))
Varascii = 65

for j in range(Varrows):
    for l in range(j+1):
        Varalpha = chr(Varascii)
        print(Varalpha, end=" ")
        Varascii += 1
    print()  

