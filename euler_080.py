from time import time
from decimal import Decimal, getcontext

getcontext().prec = 102

def digital_sum(s):
    return sum([int(c) for c in s])

start = time()

ds = 0

for n in range(101):
    sq = str(Decimal(n).sqrt()).replace(".", "")[:100]
    if len(sq) == 100:
        ds += digital_sum(sq)

print("Total digital sum: " + str(ds))

stop = time()
print("Time: " + str(stop - start))