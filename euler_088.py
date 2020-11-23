from time import time
from numpy import prod

def is_ps(t):
    return sum(t) == prod(t)

def product_sum_tuple(t):
    p = prod(t)
    s = sum(t)
    k = p - s
    l = len(t) + k

    return (l, p)


start = time()

# Non-trivial divisor of all numbers up to 24000
divisors = {n:[] for n in range(2, 24001)}

for d in range(2, 12001):
    k = 2 * d
    while k < 24001:
        divisors[k].append(d)
        k += d

# All non-trivial decompositions of n
def decomp(n):
    divs = divisors[n]

    if len(divs) == 0:
        return []

    if len(divs) == 1:
        return [(divs[0], n // divs[0])]

    comps = []

    for d in divs:
        comps.append(tuple(sorted((d, n // d))))
        for t in decomp(n // d):
            comps.append(tuple(sorted([d] + sorted(t))))

    return set(comps)


factorizations = {n:decomp(n) for n in range(2, 24001)}

# All set sizes given a product sum number n
set_sizes = {n:set() for n in range(2, 24001)}

for n in range(2, 24001):
    for f in factorizations[n]:
        set_sizes[n].add(product_sum_tuple(f)[0])

# All product sum numbers given a set size
psn = {k:set() for k in range(2, 12001)}

for n in range(2, 24001):
    for s in set_sizes[n]:
        if s < 12001:
            psn[s].add(n)


# Unique minimal product sum numbers
unique_minimal = set()

for s in psn.values():
    if s:
        unique_minimal.add(min(s))


print("Sum of minimal product sum numbers: ", sum(unique_minimal))

stop = time()
print("Time: " + str(stop - start))