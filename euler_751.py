from time import time
from decimal import Decimal, getcontext, ROUND_FLOOR
from typing import Generator

getcontext().prec = 102
#getcontext().rounding = ROUND_FLOOR

def generate(phi: Decimal) -> Generator[Decimal, None, None]:
    b = phi
    a = round(b,0)
    while True:
        yield a
        b = round(b,0)*(b - round(b,0) + Decimal(1))
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
    new_candidates = [Decimal(str(c)[:digits] + str(d)) for c in candidates for d in range(10)]
    new_candidates.sort(key=lambda x: (concatenate(x)-x))
    smallest_positive = list(filter(lambda x: x > 0, new_candidates))[0]
    smallest_index = new_candidates.index(smallest_positive)
    return [new_candidates[smallest_index], new_candidates[smallest_index + 1]]

start = time()

candidates = [Decimal("2." + str(d)) for d in range(10)]
for d in range(4):
    candidates = add_digit(candidates, d + 3)
print(candidates)


end = time()
print("Time: " + str(end - start) + " seconds")