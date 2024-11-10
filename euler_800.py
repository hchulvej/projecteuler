from time import time
from math import log, exp, comb
from gmpy2 import next_prime

def prime_gen():
    n = 5
    while True:
        yield n
        n = next_prime(n)

def log_power(a,b):
    return log(a) * b + a * log(b)

start = time()

primes = [2, 3]
pg = prime_gen()

limit = 800
n = limit * log(limit)

prime_limit = log_power(primes[-1], primes[-2])


while prime_limit < n:
    primes.append(next(pg))
    prime_limit = log_power(primes[-1], primes[-2])


f = dict(zip(primes, [0]*len(primes)))

for p in primes:
    for i in range(primes.index(p) + 1, len(primes)):
        if log_power(p, primes[i]) > limit:
            f[p] = primes[i - 1]
            break

print(f)

end = time()
print("Time: " + str(end - start) + " seconds")