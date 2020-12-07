from time import time
from primesieve import Iterator
import numpy as np

it = Iterator()

start = time()

prime_divisors = {n : set() for n in range(2, 100001)}

p = 0

while p < 100000:

    p = it.next_prime()
    k = p

    while k < 100001:
        prime_divisors[k].add(p)
        k += p

radicals = {n : np.prod(list(prime_divisors[n])) for n in range(2, 100001)}

s_radicals = [(1, 1)] + sorted(radicals.items(), key = lambda kv: (kv[1], kv[0]))

print("E(10000) =", s_radicals[9999][0])


stop = time()

print("Time: ", stop - start)