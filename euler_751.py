from time import time
from math import floor

def gen(phi):
    b = phi
    a = floor(b)
    while True:
        yield a
        b = floor(b) * (b - floor(b) + 1)
        a = floor(b)

def concatenated(phi):
    g = gen(phi)
    before = str(next(g)) + "."
    after = ""
    while len(after) < 24:
        after += str(next(g))
    return before + after[0:24]

def difference(phi):
    return float(concatenated(phi)) - phi

start = time()

def add_digit(l: list[float]) -> list[float]:
    d = len(str(l[0]))
    candidates = [(f +float(t/(10**(d-2))), difference(f +float(t/(10**(d-2))))) for t in range(1, 10) for f in l]
    candidates.sort(key=lambda x: abs(x[1]))
    return [c[0] for c in candidates[:2]]

phi_ex = 2.0
candidates = add_digit([phi_ex])
candidates = add_digit(candidates)
print(candidates)

end = time()
print("Time: " + str(end - start) + " seconds")