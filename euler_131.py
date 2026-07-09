import gmpy2 as g
from time import time

start = time()

# First some math
#
# The cube root of a rational number (a / b) is rational itself
# iff a and b are perfect cubes
#
# n^3 + p*n^2 = k^3 <=> n^3*((n + p) / n) = k^3 <=>
# cube root of (n + p) / n is k / n, which is rational
# so n + p and n are perfect cubes
#
# That is, p is the difference between two perfect cubes:
#
# p = a^3 - b^3 = (a - b)(a^2 + ab + b^2) WLOG a > b > 0
#
# Since a - b < a^2 + ab + b^2, and p is a prime,
# a - b = 1
#
# We are looking for primes that can be written as p = (m + 1)^3 - m^3 = 3m^2 + 3m + 1
#
# We have p < 1000000, so m < 1000

count = 0
for m in range(1, 1000):
    p = (m + 1)**3 - m**3
    if p < 1000000 and g.is_prime(p):
        count += 1


end = time()
print("Time: " + str(end - start) + " seconds")
print("Number of primes: " + str(count))