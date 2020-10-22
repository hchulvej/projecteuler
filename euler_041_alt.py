from time import time
import primesieve
from primesieve import *
from itertools import permutations

def is_prime(n):
    return (n in [2, 3]) or (n in n_primes(2,n-1))

def perm_to_int(perm):
    res = ""
    for p in perm:
        res += p
    return int(res)

start = time()

largest = 2

for n in range(1,10):
    perms = permutations("123456789"[:n],n)
    for p in perms:
        q = perm_to_int(p)
        if is_prime(q) and q > largest:
            largest = q

print("Largest pandigital prime is: " + str(largest))

stop = time()
print("Time: " + str(stop-start))