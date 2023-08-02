Var_str = "My father is very not smart. Just kidding."

Var_words = [word.lower() for word in Var_str.split()]

Var_words.sort()

print("The sorted words are:")

for w in Var_words:
    print(w)


