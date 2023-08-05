try:
 print('this is try block')
 varx=int(input("Enter a number:"))
 vary=int(input("Enter second number:"))
 varz=varx/vary
except ZeroDivisionError:
 print("You are trying to divide a number by zero")
 print("Which is not possible hence error generated")
else:
 print("this is else block")
 print("The division value is=", varz)
finally:
 print("This is finally block")
 varx=0
 vary=0
print("This is out side the try except block")