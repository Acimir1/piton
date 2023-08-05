class strprint():
 def __init__(self):
  self.string=""

 def funcget(self):
  self.string=input("Enter a string:")

 def funcput(self):
  print("The string entered by user is:", self.string)

obj1=strprint()
obj1.funcget()
obj1.funcput()