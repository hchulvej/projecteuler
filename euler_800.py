from time import time
from math import log, exp, comb
from gmpy2 import next_prime

def prime_gen():
    n = 5
    while True:
        yield n
        n = next_prime(n)

start = time()

primes = [2, 3]
pg = prime_gen()

limit = 800
n = limit * log(limit)

prime_limit = primes[-1]*log(primes[-1]) + primes[-2]*log(primes[-2])

while prime_limit < n:
    primes.append(next(pg))
    prime_limit = primes[-1]*log(primes[-1]) + primes[-2]*log(primes[-2])


print(n, prime_limit)

end = time()
print("Time: " + str(end - start) + " seconds")