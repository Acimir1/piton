def Varmod(vlist, key1):
 return [i.get(key1) for i in vlist]

Vardict1 = [{'name' : 'Python', 'version': 4},
{'name': 'JAVA', 'version': 17},
{'name': 'Machine Learning', 'version':18},
{'name': 'R Programming', 'version': 10}]

print(Varmod(Vardict1, 'version'))
