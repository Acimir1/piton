Varx = [[1,2,3],[4,5,6],[7,8,9]]
Vary = [[2,3,4],[5,6,7],[8,9,1]]
Varresult = [[Varx[j][k] + Vary[j][k] for j in range(len(Varx[0]))] for k in range(len(Varx))]

for l in Varresult:
    print(l)