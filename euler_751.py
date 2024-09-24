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

phi_ex = 2.21
print([(float("2."+str(t)), difference(float("2."+str(t)))) for t in range(1, 10)])

end = time()
print("Time: " + str(end - start) + " seconds")