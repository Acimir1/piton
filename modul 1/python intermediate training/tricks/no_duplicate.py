from collections import Counter

def FuncRemove_dup(Varinput):
 Varinput = Varinput.split(" ")

 for j in range(0, len(Varinput)):
  Varinput[j] = "".join(Varinput[j])
 Varuniq = Counter(Varinput)

 vars = " ".join(Varuniq.keys())
 print(vars)

Varinput = "This is a program to remove duplicates values. remove In this program word is duplicate"
FuncRemove_dup(Varinput)