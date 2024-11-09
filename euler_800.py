from time import time
from scipy.special import lambertw
from math import log, exp, comb
from sympy import primerange

start = time()

limit = 800
n = limit * log(limit)
prime_limit = 1000
primes = list(primerange(2, prime_limit + 1))
p = primes[-2]
q = primes[-1]
h = (p ** q) * (q ** p)
print(log(h) >= n)

end = time()
print("Time: " + str(end - start) + " seconds")