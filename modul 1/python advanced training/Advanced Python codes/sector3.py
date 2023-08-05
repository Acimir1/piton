import time
vars_time = time.time()
vartotal = 0
for i1 in range(50000):
 vartotal = vartotal+i1
vare_time = time.time() - vars_time
print(vare_time)