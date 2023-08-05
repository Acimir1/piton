Vars = (str(input("Enter name of text file: ")))
Varfile = open(Vars, 'r')
Varline = Varfile.readline()
while(Varline != ""):
    print(Varline)
    Varline = Varfile.readline()
Varfile.close