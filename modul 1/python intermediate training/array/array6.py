import sys

def push(Varelement, Varsize, Varstack):
 global Vartop
 if Vartop >= Varsize - 1:
  print("Stack is Overflow")
 else:
  Vartop += 1
  Varstack[Vartop] = Varelement


def pop():
 global Vartop
 if Vartop < 0:
  print("Stack Underflow")
  sys.exit()
 else:
  Varelement = Varstack[Vartop]
  print('%s' % Varelement, end='')
  Vartop -= 1

def func_reversesort(Varstring):
 Varstring = list(Varstring)
 Varstr = ''

 for j in reversed(Varstring):
  Varstr += j

 return Varstr

Varsize = 12
Varstack = [0]*Varsize
Varstring = 'PythonString'
Vartop = -1

push('P', 12, Varstack)
push('y', 12, Varstack)
push('t', 12, Varstack)
push('h', 12, Varstack)
push('o', 12, Varstack)
push('n', 12, Varstack)
push('S', 12, Varstack)
push('t', 12, Varstack)
push('r', 12, Varstack)
push('i', 12, Varstack)
push('n', 12, Varstack)
push('g', 12, Varstack)

print('Original Stack  %s' %Varstring)
print("Performing Stack")
print('Reversed String = ', end='')
for j in Varstack:
 pop()
print("\n")
print("Performing Sort()")
print("\n")
print("Reversed String is %s " %func_reversesort(Varstring))
