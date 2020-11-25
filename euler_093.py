from time import time
from itertools import combinations_with_replacement, combinations, permutations

def two_way(a, b, o):
    if o == 0:
        return a + b
    if o == 1:
        return a - b
    if o == 2:
        return a * b
    if o == 3:
        return a / b


def three_way(a, b, c, o):
    if o in [(0, 2), (0, 3), (1, 2), (1, 3)]:
        return two_way(a, two_way(b, c, o[1]), o[0])
    else:
        return two_way(two_way(a, b, o[0]), c, o[1])

def four_way(a, b, c, d, o):
    if o[0] > 1:
        m = two_way(a, b, o[0])
        if o[1] < 2:
            return two_way(m, two_way(c, d, o[2]), o[1])
        else:
            return two_way(m, two_way(c, d, o[2]), o[1])
    else:
        return two_way(a, three_way(b, c, d, (o[1], o[2])), o[0])

def is_int(n):
    return 1.0 * n - int(n) == 0.0

def combinations2(nt, ot):
    a, b, c, d = nt[0], nt[1], nt[2], nt[3]
    comb = set()

    # a * b * c * d
    m = four_way(a, b, c, d, ot)
    if is_int(m) and m > 0:
        comb.add(int(m))

    # a * (b * c * d)
    m = two_way(a, three_way(b, c, d, (ot[1], ot[2])), ot[0])
    if is_int(m) and m > 0:
        comb.add(int(m))

    # (a * b * c) * d
    m = two_way(three_way(a, b, c, (ot[0], ot[1])), d, ot[2])
    if is_int(m) and m > 0:
        comb.add(int(m))

    # ((a * b) * c) * d
    m = two_way(two_way(two_way(a, b, ot[0]), c, ot[1]), d, ot[2])
    if is_int(m) and m > 0:
        comb.add(int(m))

    # (a * (b * c)) * d
    m = two_way(two_way(a, two_way(b, c, ot[1]), ot[0]), d, ot[2])
    if is_int(m) and m > 0:
        comb.add(int(m))

    # a * ((b * c) * d)
    m = two_way(a, two_way(two_way(b, c, ot[1]), d, ot[2]), ot[0])
    if is_int(m) and m > 0:
        comb.add(int(m))

    # a * (b * (c * d))
    m = two_way(a, two_way(b, two_way(c, d, ot[2]), ot[1]), ot[0])
    if is_int(m) and m > 0:
        comb.add(int(m))

    # (a * b) * (c * d)
    m = two_way(two_way(a, b, ot[0]), two_way(c, d, ot[2]),ot[1])
    if is_int(m) and m > 0:
        comb.add(int(m))

    # a * (b * c) * d
    m = three_way(a, two_way(b, c, ot[1]), d, (ot[0], ot[2]))
    if is_int(m) and m > 0:
        comb.add(int(m))

    # a * b * (c * d)
    m = three_way(a, b, two_way(c, d, ot[2]), (ot[0], ot[1]))
    if is_int(m) and m > 0:
        comb.add(int(m))

    # (a * b) * c * d
    m = three_way(two_way(a, b, ot[0]), c, d, (ot[1], ot[2]))
    if is_int(m) and m > 0:
        comb.add(int(m))



    return comb




start = time()

longest = ((0,0,0,0),0)

for ns in combinations([0,1,2,3,4,5,6,7,8,9], 4):

    nums = []

    for nt in permutations(ns):
        for otc in combinations_with_replacement([0,1,2,3], 3):
            for ot in permutations(otc):
                try:
                    nums += [c for c in combinations2(nt, ot)]
                except:
                    continue

    if 1 in nums:
        k = 2
        while k in nums:
            k += 1

    if longest[1] < k - 1:
        longest = (sorted(ns), k - 1)


print("Set with longest chain: ", longest[0])

stop = time()

print("Time: ", stop - start)