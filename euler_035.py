from time import time
from primesieve.numpy import *

def circulate(p):
    res = set()
    n = len(str(p))
    for k in range(n):
        res.add(int("".join([str(p)[(k+i)%n] for i in range(n)])))
    return res

start = time()

prime_candidates = primes(10**6)

circular = 0

for p in prime_candidates:
    if all([(q in prime_candidates) for q in circulate(p)]):
        circular += 1

print("Number of circular primes: " + str(circular))

stop = time()
print("Time: " + str(stop-start))