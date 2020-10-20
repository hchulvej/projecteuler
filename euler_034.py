from time import time
from math import factorial

def sum_fac_dig(n):
    return sum(set(map(factorial,[int(d) for d in str(n)])))

start = time()

facs = [factorial(n) for n in range(10)]

def sum_fac_dig(n):
    return sum([facs[int(d)] for d in str(n)])

for i in range(10,2540160):
    if sum_fac_dig(i) == i:
        print(i)

stop = time()
print("Time: " + str(stop-start))