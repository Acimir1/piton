Varx = [[3,6],[5,6],[7,8]]
Varresult = [[0,0,0],[0,0,0]]
for j in range(len(Varx)):
 for k in range(len(Varx[0])):
  Varresult[k][j] = Varx[j][k]

for l in Varresult:
 print(l)
