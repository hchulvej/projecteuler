from time import time
from decimal import Decimal, getcontext, ROUND_FLOOR
from typing import Generator

getcontext().prec = 102
getcontext().rounding = ROUND_FLOOR

def generate(phi: Decimal) -> Generator[Decimal, None, None]:
    b = phi
    a = round(b,0)
    while True:
        yield a
        b = round(b,0)*(b - round(b,0) + 1)
        a = round(b,0)

def concatenate(phi: Decimal) -> Decimal:
    g = generate(phi)
    s = str(next(g)) + "."
    ls = len(s)
    while len(s) < 24 + ls:
        s += str(next(g))
    s = s[:24 + ls]
    return Decimal(s)

def add_digit(candidates: list[Decimal], digits: int) -> list[Decimal]:
    new_candidates = [round(Decimal(str(c) + str(d)), digits) for c in candidates for d in range(10)]
    return new_candidates

start = time()

print(add_digit([Decimal(2.1)], 3))


end = time()
print("Time: " + str(end - start) + " seconds")