from time import time
from itertools import product

start = time()

primes = [2, 3, 5, 7, 11, 13, 17]

def factors(t):
    res = 1
    for i in range(len(t)):
        res *= 2 * t[i] + 1
    return res

def prime(t):
    p = 1
    for i in range(len(t)):
        p *= primes[i] ** t[i]
    return p

powers = []

for t in product([0, 1, 2], repeat=7):
    if factors(t) > 2000:
        powers.append(t)


minimal_product = prime(powers[0])

for i in range(1, len(powers)):
    if prime(powers[i]) < minimal_product:
        minimal_product = prime(powers[i])

print("Least value of n:", minimal_product)

stop = time()
print("Time: " + str(stop - start))