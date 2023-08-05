class calc():
 def __init__(self,i1,i2):
  self.i1=i1
  self.i2=i2
 def funcadd(self):
  return self.i1 + self.i2
 def funcmul(self):
  return self.i1 * self.i2
 def funcdiv(self):
  return self.i1 / self.i2
 def funcsub(self):
  return self.i1 - self.i2

i1 = int(input("Enter the first number:"))
i2 = int(input("Enter the second number:"))
obj1=calc(i1,i2)
varchoice = 1
while varchoice!=0:
 print("0. Exit")
 print("1. Add")
 print("2. Subtract")
 print("3. Multiply")
 print("4. Divide")
 varchoice = int(input("Enter your choice:"))
 if varchoice==1:
  print("The result is:", obj1.funcadd())
 elif varchoice==2:
  print("The result is:", obj1.funcsub())
 elif varchoice==3:
  print("The result is:", obj1.funcmul())
 elif varchoice==4:
  print("The result is:", round(obj1.funcdiv(),2))
 elif varchoice==0:
  print("Exiting the program!!!")
 else:
  print("Invalid choice")
