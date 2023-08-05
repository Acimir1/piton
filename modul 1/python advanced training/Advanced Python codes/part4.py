class clsnode:
 def __init__(self, vardata):
  self.vardata = vardata
  self.varnext = None

class clsLinkedList:
 def __init__(self):
  self.varhead = None
  self.varlast_node = None

 def funcappend(self, vardata):
  if self.varlast_node is None:
   self.varhead = clsnode(vardata)
   self.varlast_node = self.varhead
  else:
   self.varlast_node.varnext = clsnode(vardata)
   self.varlast_node=self.varlast_node.varnext

 def funcdisplay(self):
  varcurrent = self.varhead
  while varcurrent is not None:
   print(varcurrent.vardata, end=' ')
   varcurrent = varcurrent.varnext

varllist = clsLinkedList()
varn = int(input("How many elements do you want to enter in linked list:"))
for i1 in range(varn):
 vardata = int(input("Enter data value:"))
 varllist.funcappend(vardata)
print('The linked list is :',end=' ')
varllist.funcdisplay()