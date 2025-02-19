from time import time
from math import log
from gmpy2 import next_prime

# Reasoning:
#
# p^q * q^p <= n = a^b <=> q*log(p)+p*log(q) <= b*log(a)
#
# For a given prime p, we want to count the number of primes q > p such that q^p * p^q <= n
# or q*log(p)+p*log(q) <= b*log(a)
#
# A lower limit on q is p + 1
#
# and an upper limit is (b*log(a))/log(p), since q*log(p)+p*log(q) <= b*log(a) => q < (b*log(a))/log(p)
#
# The function q -> q*log(p)+p*log(q) is increasing, so we can use binary search to find the number of primes q > p such that q*log(p)+p*log(q) <= b*log(a).

def suitable_q(p, b, a, q):
    return q * log(p) + p * log(q) <= b * log(a)

def prime_gen():
    n = 5
    while True:
        yield n
        n = next_prime(n)

start = time()

a = 800
b = 800
ul = int(b * log(a) / log(2))

print("Upper limit: " + str(ul))

pg = prime_gen()

primes = [2, 3]
while primes[-1] < ul:
    primes.append(next(pg))

end = time()
print(str(len(primes)) + " primes generated.")
print("Time: " + str(end - start) + " seconds")

suitable_qs = dict(zip(primes, [0] * len(primes)))

print("Test prime =", primes[100], " limit =", int(b * log(a) / log(primes[100])))

for i in range(len(primes)-1):
    if suitable_q(primes[100], b, a, primes[i]) and not suitable_q(primes[100], b, a, primes[i+1]):
        print("Largest q is", str(primes[i]))

    


end = time()
print("Time: " + str(end - start) + " seconds")