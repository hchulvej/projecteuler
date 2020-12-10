from time import time
from itertools import combinations, chain, product

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

A_five = [6, 9, 11, 12, 13]
A_six = [11] + [11 + a for a in A_five]
A_seven = [20] + [20 + a for a in A_six]

optimal = []
optimal_sum = 10 ** 6


plus_minus_two = [-2, -1, 0, 1, 2]
for c in product(plus_minus_two, repeat=7):

    new_set = [A_seven[i] + c[i] for i in range(7)]
    if check_prop_one(new_set) and check_prop_two(new_set):
        if sum(new_set) < optimal_sum:
            optimal = new_set
            optimal_sum = sum(new_set)

print("".join(list(map(str, sorted(optimal)))), optimal_sum)

stop = time()

print("Time: ", stop - start)