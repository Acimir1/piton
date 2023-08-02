import random

while True:
 input("Press enter to roll the dice")
 Varnum = random.randint(1,10)
 print("The number is:" ,Varnum)
 Varch = input("Do you want to Roll Again? (Y/N)")
 if Varch=='n':
  break