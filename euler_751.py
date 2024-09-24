from time import time
from math import floor
from gmpy2 import mpfr
from typing import Generator

def gen(phi: mpfr) -> Generator[mpfr, None, None]:
    b = phi
    a = mpfr(floor(b))
    while True:
        yield a
        b = mpfr(floor(b)) * mpfr(b - mpfr(floor(b)) + mpfr(1))
        a = mpfr(floor(b))

def concatenated(phi: mpfr) -> mpfr:
    g = gen(phi)
    before = str(next(g)) + "."
    after = ""
    while len(after) < 24:
        after += str(next(g))
    return mpfr(before + after[0:24])

def difference(phi: mpfr) -> mpfr:
    return mpfr(concatenated(phi)) - phi

def add_decimal(phi: mpfr, d: int) -> mpfr:
    after = str(phi - mpfr(2))[1:]
    added = mpfr("0." + "0"*len(after) + str(d))
    return phi + added

start = time()

phi = mpfr(2.2)
print(phi, add_decimal(phi, 5))

end = time()
print("Time: " + str(end - start) + " seconds")