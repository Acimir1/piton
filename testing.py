print("Hello World!")

trokut = "*"

for i in range(6):
    print(trokut, end="\n")
    trokut = "*" + trokut + "*"

# import pyodbc 

# SERVER = '127.0.0.1'
# DATABASE = 'testing'
# USERNAME = 'sa'
# PASSWORD = 'Pa55w0rD'

# connectionString = ("Driver={SQL Server Native Client 11.0};"
#             "Server=127.0.0.1;"
#             "Database=testing;"
#             "UID=sa;"
#             "PWD=Pa55w0rD;")
# conn = pyodbc.connect(connectionString)

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM Artist WHERE ArtistID = 1')

# for row in cursor:
#     print('row = %r' % (row,))

import random

print("DOBRODOŠLI U NAŠU IGRU 'POGODI BROJ'!!")
print("Pravila su jednostavna, pogodite broj i dobit ćete VELIKU nagradu")
print("ali, ako fulate broj, SRETNO hehe")
print("Imate 3 pokušaja")
x = input("Razumijete li pravila:[Y/N]")

if x == "Y" or x == "y":
    y = random.randint(1,100)
    for i in range(3):
        z = int(input("Unesite broj od 1 do 100: "))
        if z == y:
            print("ČESTITAMO!!")
            break
        elif z != y:
            print("Netočno, pokušajte ponovno")



