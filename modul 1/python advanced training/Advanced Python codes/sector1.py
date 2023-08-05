import os

varpath = os.getcwd()
print("function os.getcwd()")
print(varpath)

os.chdir('E:\\')
varpath = os.getcwd()
print("Function os.chdir()")
print(varpath)

varstr = os.listdir('E:\\Python Codes')
print("function os.listdir()")
print(varstr)

varstr2 = [entry for entry in varstr if entry.endswith('.txt')]
print("only text files")
print(varstr2)

os.rename('E:\\Python Code\\one.txt', 'E:\\Python Code\\newone.txt')

varstr=os.listdir()
print(varstr)