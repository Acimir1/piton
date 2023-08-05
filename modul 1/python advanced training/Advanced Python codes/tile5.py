try:
 varx=int(input("enter a number less then 100:"))
 if varx>100:
  raise ValueError(varx)
except ValueError:
 print(varx," is out of the given range")
else:
 print(varx," is within the allowed range")