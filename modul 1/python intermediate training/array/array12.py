Var_str = "This is Python to Sort the Words as per Alphabetical Order"

Var_words = [word.lower() for word in Var_str.split()]

Var_words.sort()

print("The sorted words are:")
for w in Var_words:
 print(w)
