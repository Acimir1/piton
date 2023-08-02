Varx = [[11,9,2],[5,6,7],[8,9,1]]
Vary = [[4,7,2],[5,7,8],[3,6,7]]
Varresult = [[0,0,0],[0,0,0],[0,0,0]]

for j in range(len(Varx)):
 for k in range(len(Varx[0])):
  Varresult[j][k] = Varx[j][k] + Vary[j][k]

for l in Varresult:
 print(l)