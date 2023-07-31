Varrpunc = ["!", "-", ".", ",", "&", "/", "(", ")", "=", "?"]
VarStr = "Hello!!! Welcome to Python ---- This is next Course!!!!!,."

Varno_punc = ""
for j in VarStr:
    if j not in Varrpunc:
        Varno_punc = Varno_punc + j

print("Varno_punc je" + " " + Varno_punc)