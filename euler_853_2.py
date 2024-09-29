from time import time
from sympy import lcm, factorint
from functools import reduce

periods = dict()

def basic_pisano(n: int) -> int:
    if n in periods:
        return periods[n]
    if n < 2:
        return 1
    else:
        a, b = 1, 1
        i = 1
        while a != 0 or b != 1:
            a, b = b, (a + b) % n
            i += 1
        periods[n] = i
        return i


def prime_power_pisano(p:int, k: int) -> int:
    if p**k in periods:
        return periods[p**k]
    periods[p**k] = p**(k-1)*basic_pisano(p)
    return periods[p**k]


def coprime_pisano(n: int, m: int) -> int:
    if n*m in periods:
        return periods[n*m]
    periods[n*m] = lcm(basic_pisano(n), basic_pisano(m))
    return periods[n*m]

def pisano(n: int) -> int:
    if n in periods:
        return periods[n]
    periods[n] = reduce(lcm, (prime_power_pisano(prime, mult) for prime, mult in factorint(n).items()), 1)
    return periods[n]

# If n > 2 and L_t <= n, then pi(n) >= 2t
# L_60 = 29075380
# L_61 = 38516678
# I.e. if n >= 38516678, then pi(n) >= 122
# We limit n to be < 38516678
start = time()
sum = 0
for n in range(2, 38516678):
    if pisano(n) == 120:
        sum += n



end = time()
print("Sum: " + str(sum))
print("Time: " + str(end - start) + " seconds")