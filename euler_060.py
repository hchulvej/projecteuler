from time import time
from math import sqrt
from primesieve import Iterator
from primePy import primes



def is_prime(n):
    it = Iterator()
    p = it.next_prime()

    lim = int(sqrt(n)) + 1
    while p < lim:
        if n % p == 0:
            return False
        p = it.next_prime()
    return True


def is_prime_pair(p, q):
    return is_prime(int(str(p) + str(q))) and is_prime(int(str(q) + str(p)))


start = time()

p_list = list(primes.upto(10000))
l = len(p_list)

pairs = {}
for p in p_list:
    pairs[p] = set()

for p in p_list:
    for q in p_list:
        if is_prime_pair(p, q):
            pairs[p].add(q)
            pairs[q].add(p)

candidates = [p for p in pairs if len(pairs[p]) > 4]

threes = set()

for a in candidates:
    for b in pairs[a]:
        for c in candidates:
            if c in pairs[a].intersection(pairs[b]):
                threes.add((a,b,c))

fours = set()

for t in threes:
    for c in candidates:
        if c in t:
            continue
        else:
            if c in pairs[t[0]].intersection(pairs[t[1]]).intersection(pairs[t[2]]):
                fours.add((t[0], t[1], t[2], c))

fives = set()

for q in fours:
    for c in candidates:
        if c in q:
            continue
        else:
            if c in pairs[q[0]].intersection(pairs[q[1]]).intersection(pairs[q[2]]).intersection(pairs[q[3]]):
                fives.add((q[0], q[1], q[2], q[3], c))

lowest_sum = 50000
lowest = (0,0,0,0,0)

for f in fives:
    if sum(f) < lowest_sum:
        lowest_sum = sum(f)
        lowest = f

print("Optimal set of  five: " + str(lowest) + ", sum: " + str(lowest_sum))



stop = time()
print("Time: " + str(stop - start))