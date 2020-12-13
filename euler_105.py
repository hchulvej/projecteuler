from time import time
from itertools import combinations, chain

def powerset(S):
    return list(map(list, chain.from_iterable(combinations(S, r) for r in range(1, len(S)))))

def check_prop_one(S):
    for c in combinations(powerset(S), 2):
        if sum(c[0]) == sum(c[1]):
            return False
    return True

def check_prop_two(S):
    for c in combinations(powerset(S), 2):
        if len(c[0]) < len(c[1]) and sum(c[0]) >= sum(c[1]):
            return False
    return True

start = time()

with open("p105_sets.txt", "r") as f:
    raw = f.readlines()
    raw = [list(map(int, r.replace("\n", "").split(","))) for r in raw]


total = 0

for r in raw:
    if check_prop_one(r) and check_prop_two(r):
        total += sum(r)

print("Total sum is:", total)

stop = time()
print("Time: " + str(stop - start))