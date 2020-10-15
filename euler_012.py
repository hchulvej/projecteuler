from time import time
from primePy import primes
from collections import Counter

def triangle():
    n = 1
    while True:
        yield int(n*(n+1)/2)
        n += 1

tri_gen = triangle()

def number_of_factors(n):
    num = 1
    for i in Counter(primes.factors(n)).values():
        num *= i+1
    return num

start = time()
t = next(tri_gen)
while True:
    if number_of_factors(t) > 500:
        print("First triangle number with more than 500 divisors: " + str(t))
        break
    t = next(tri_gen)


stop = time()
print("Time: " + str(stop-start))