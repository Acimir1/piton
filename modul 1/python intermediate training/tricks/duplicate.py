Varstr = "This program is to find duplicate word . Here program word is duplicate"
Varlen = Varstr.split()
Vark=[]
for j in Varlen:
 if(Varstr.count(j)>=1 and (j not in Vark)):
  Vark.append(j)
print(' '.join(Vark))