from time import time
from math import ceil, gcd, sqrt

def primitive_generators(L):
    gens = []
    for m in range(1, ceil(sqrt(L/2))):
        if m%2 == 0:
            for n in range(1, m, 2):
                if 2 * m * (m + n) <= L and gcd(n, m) == 1:
                    gens.append((n, m))
        else:
            for n in range(2, m, 2):
                if 2 * m * (m + n) <= L and gcd(n, m) == 1:
                    gens.append((n, m))
    return gens

def perimeters(g, L):
    n = g[0]
    m = g[1]
    l = 2 * m * (m + n)
    return [k * l for k in range(1, L // l + 1)]

start = time()

pg = primitive_generators(1500000)

f = {g:perimeters(g, 1500000) for g in pg}

counts = [0] * 1500001

for g in pg:
    for p in f[g]:
        counts[p] += 1

print("Number of unique perimeters: " + str(len([p for p in range(1500001) if counts[p] == 1])))


stop = time()
print("Time: " + str(stop-start))