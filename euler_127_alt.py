from time import time
from primesieve import primes
from math import gcd

# Numbers a, b, c are assumed to have no common prime factors
def rad(a, b, c):
    return rads[a] * rads[b] * rads[c]

start = time()

limit = 120000

# List of primes less than limit
p_list = primes(limit)

# Radicals of numbers less than limit
rads = {n : 1 for n in range(limit)}
for p in p_list:
    k = p
    while k < limit:
        rads[k] *= p
        k += p

total = 0

for c in [n for n in range(1, limit) if not 2 * rads[n] >= n]:
    for b in range(1, c):
        a = c - b
        if a < b and gcd(rads[a], rads[b]) == 1 and rad(a, b, c) < c:
            total += c

print(total)

stop = time()
print("Time: ", stop - start)