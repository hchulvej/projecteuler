from time import time
from primePy import primes
from math import sqrt

start = time()

limit = 10000

primenums = set(primes.upto(limit))
twas = set(2*n*n for n in range(int(sqrt(limit/2) + 1)))
odd_comp = set(2 * k + 1 for k in range(int(limit/2) + 1) if not 2 * k - 1 in primenums)

sums = set()

for p in primenums:
    for t in twas:
        sums.add(p + t)

print(set(o for o in odd_comp if o not in sums))


print("Composite number: " + str(0))

stop = time()
print("Time: " + str(stop-start))