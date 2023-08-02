from heapq import nlargest
Vardict={'P1': 400, 'P2': 120, 'P3': 450, 'P4': 128,'P5':506,'P6':890,'P7':12,'P8':895,'P9':238,'P10':843}

fifthl = nlargest(5, Vardict, key=Vardict.get)
print(fifthl)