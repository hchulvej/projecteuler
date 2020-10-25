from time import time
from primePy import primes
from collections import Counter
from itertools import count


def pfs(n):
    return set(f for f in Counter(primes.factors(n)).most_common())

def four_cons(n):
    res = pfs(n)
    for i in range(1,4):
        res = res.union(pfs(n + i))
    return res

start = time()

for n in count(1):
    if len(four_cons(n)) == 16:
        print("First of four consecutive numbers: " + str(n))
        break


stop = time()
print("Time: " + str(stop-start))