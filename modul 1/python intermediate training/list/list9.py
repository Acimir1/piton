from itertools import groupby
from operator import itemgetter

Varlist = ['banana', 'apple', 'line', 'good', 'be','bite', 'an', 'and', 'cucumber', 'goat', 'zebra', 'pen', 'black', 'pipe', 'mine', 'nine', 'mango', 'nice']

for l, w in groupby(sorted(Varlist), key=itemgetter(0)):
 print(l)
 for w1 in w:
  print(w1)