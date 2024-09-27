from time import time
from decimal import Decimal, getcontext
from math import floor
from typing import Generator

getcontext().prec = 102


def generate(phi: Decimal) -> Generator[Decimal, None, None]:
    b = phi
    a = floor(b)
    while True:
        yield a
        b = floor(b)*(b - floor(b) + Decimal(1))
        a = floor(b)

def concatenate(phi: Decimal) -> Decimal:
    g = generate(phi)
    s = str(next(g)) + "."
    ls = len(s)
    while len(s) < 24 + ls:
        s += str(next(g))
    s = s[:24 + ls]
    return Decimal(s)

def diff(phi: Decimal) -> Decimal:
    return concatenate(phi) - phi


def add_digit(smallest_positive: str) -> Decimal:
    cs = [Decimal((smallest_positive + str(d))) for d in range(10)]
    dfs = list(filter(lambda x: diff(x) >= 0, cs))
    dfs = sorted(dfs, key=diff)
    return Decimal(str(dfs[0]))

d = "2."
while len(d) < 24 + 2:
    d = str(add_digit(d))
print(d)

start = time()




end = time()
print("Time: " + str(end - start) + " seconds")