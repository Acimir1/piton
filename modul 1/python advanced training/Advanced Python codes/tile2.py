try:
 vara=80
 varb=2
 print(vara/varb)
except TypeError:
 print("Unsupported Operation")
except ZeroDivisionError:
 print("Divide by zero error has occurred")
print("Outside try except block")