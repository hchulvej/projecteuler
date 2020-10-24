from time import time
from math import sqrt


def is_integer(f):
    return f-int(f) == 0.0

def is_pentagonal(i):
    return is_integer((1 + sqrt(1 + 24*i))/6)

def is_hexagonal(i):
    return is_integer((1 + sqrt(1 + 8 * i)) / 4)

def triangular(n):
    return int(n*(n  + 1)/2)

def triple_gen():
    n = 1
    while True:
        t = triangular(n)
        if is_pentagonal(t) and is_hexagonal(t):
            yield (n, t)
        n += 1

start = time()

tg = triple_gen()

print(next(tg))
print(next(tg))
print(next(tg))


stop = time()
print("Time: " + str(stop-start))