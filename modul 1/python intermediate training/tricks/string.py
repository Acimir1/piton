Varstr = input("Enter a String:")
Varlist=[]
Varlist=Varstr.split()
Varwf = [Varlist.count(i) for i in Varlist]
print(dict(zip(Varlist,Varwf)))