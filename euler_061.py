from time import time
from itertools import permutations, product

def is_an_ordered_match(m, n):
    return n[0] != m[0] and str(n[1])[:2] == str(m[1])[2:]



start = time()

triangle = [(3, n * (n + 1) // 2) for n in range(45, 141)]
square = [(4, n**2) for n in range(32,101)]
penta = [(5, n * (3 * n - 1) // 2) for n in range(26,82)]
hexa = [(6, n * (2 * n - 1)) for n in range(23,71)]
hepta = [(7, n * (5 * n - 3) // 2) for n in range(21,64)]
octa = [(8, n * (3 * n - 2)) for n in range(19,59)]

all_n = set(triangle + square + penta + hexa + hepta + octa)

solutions = set()

for a in all_n:
    for b in [x for x in all_n if is_an_ordered_match(a, x)]:
        for c in [x for x in all_n if is_an_ordered_match(b, x)]:
            for d in [x for x in all_n if is_an_ordered_match(c, x)]:
                for e in [x for x in all_n if is_an_ordered_match(d, x)]:
                    for f in [x for x in all_n if is_an_ordered_match(e, x) and is_an_ordered_match(x, a)]:
                        if sorted([a[0], b[0], c[0], d[0], e[0], f[0]]) == [3, 4, 5, 6, 7, 8]:
                            solutions = solutions.union(set([a, b, c, d, e, f]))


print("Solution is: ")
print(solutions, sum([s[1] for s in solutions]))


stop = time()
print("Time: " + str(stop - start))