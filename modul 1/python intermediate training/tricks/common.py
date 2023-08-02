Varstr1 = input("Enter the first string: ")
Varstr2 = input("Enter the second string: ")

Vara = list(set(Varstr1)|set(Varstr2))
print("The common letters are : ")
for j in Vara:
 print(j)