import gmpy2 as g
from time import time

start = time()

# First some math
#
# If n^2 % 10 = k, then
# (n^2 + 1) % 10 = (k + 1) % 10
# (n^2 + 3) % 10 = (k + 3) % 10
# (n^2 + 7) % 10 = (k + 7) % 10
# (n^2 + 9) % 10 = (k + 9) % 10
#
# The last digit of a prime (> 5) must be odd and cannot be 5
#
# That means that n^2 % 10 must be 0.

primes = [n for n in range(15000000) if g.is_prime(100 * (n**2) + 1)]
primes = [ n for n in primes if g.is_prime(100 * (n**2) + 3)]
primes = [ n for n in primes if g.is_prime(100 * (n**2) + 7)]
primes = [ n for n in primes if g.is_prime(100 * (n**2) + 9)]
primes = [ n for n in primes if g.is_prime(100 * (n**2) + 13)]
primes = [ n for n in primes if g.is_prime(100 * (n**2) + 27)]

primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 5)]
primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 11)]
primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 15)]
primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 17)]
primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 19)]
primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 21)]
primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 23)]
primes = [ n for n in primes if not g.is_prime(100 * (n**2) + 25)]

sum = sum(primes)

end = time()
print("Time: " + str(end - start) + " seconds")
print("Sum: " + str(sum) + "0")
