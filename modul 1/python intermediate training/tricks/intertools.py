import itertools

Var_list = [[1,2],[3,4,5],[6,7,8,9]]

Var_list2 = list(itertools.chain(*Var_list))

print(Var_list2)