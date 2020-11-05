from time import time
from math import gcd

def next_f(f1, f2):
    [p, pm] = [f1[0], f2[0]]
    [q, qm] = [f1[1], f2[1]]
    d = int((q + limit) / qm)
    pmm = d * pm - p
    qmm = d * qm - q
    g = gcd(pmm, qmm)
    return (pmm // g, qmm // g)


start = time()

limit = 12000

farey = [(1, limit), (1, limit - 1)]

f = next_f(farey[-2], farey[-1])

while f[0] != f[1]:
    farey.append(f)
    f = next_f(farey[-2], farey[-1])

third = farey.index((1, 3))
half = farey.index((1, 2))

print("Number of fractions: " + str(half - third - 1))

stop = time()
print("Time: " + str(stop - start))