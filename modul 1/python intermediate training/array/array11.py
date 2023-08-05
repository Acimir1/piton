Varpunch = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

VarStr = "Hello!! Welcome to Python ---- This is Next Course!!!!,."

Varno_punch = ""
for j in VarStr:
 if j not in Varpunch:
  Varno_punch = Varno_punch + j

print(VarStr)
print(Varno_punch)
