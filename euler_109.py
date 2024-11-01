import functools
from itertools import product

values = [str(v) for v in range(1,21)]
multipliers = ["S","D", "T"]

single_throws = ["S25", "D25"]
for v in values:
    for m in multipliers:
        single_throws.append(m + v)

def throw_value(single_throw):
    if single_throw[0] == "0":
        return 0
    if single_throw[0] == "S":
        return int(single_throw[1:])
    if single_throw[0] == "D":
        return 2 * int(single_throw[1:])
    if single_throw[0] == "T":
        return 3 * int(single_throw[1:])
    return -1


def checkout_value(throws):
    total = 0
    for t in throws:
        total += throw_value(t)
    return total

def compare_throws(throw1, throw2):
    if throw1[0] == throw2[0]:
        return int(throw1[1:]) - int(throw2[1:])
    if throw1[0] == "S":
        return -1
    if throw2[0] == "S":
        return 1
    if throw1[0] == "D" and throw2[0] == "T":
        return -1
    else:
        return 1

two_first_throws = set([(t) for t in single_throws])
for t1, t2 in product(two_first_throws, two_first_throws):
    if compare_throws(t1, t2) != 1:
        two_first_throws.add((t1, t2))

two_first_throws = list(two_first_throws)


all_throws = set([t for t in two_first_throws if t[-1][0] == "D"])


for t in two_first_throws:
    for s in [s for s in single_throws if s[0] == "D"]:
        all_throws.add((*t, s))

# print([a for a in all_throws if len(a[0]) == 1])


