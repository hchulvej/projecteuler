from itertools import product
from time import time

start = time()

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

def sort_two_throws(t1, t2):
    if t1[0] == t2[0]:
        if throw_value(t1) > throw_value(t2):
            return (t2, t1)
        else:
            return (t1, t2)
    if t1[0] == "S":
        return (t1, t2)
    if t2[0] == "S":
        return (t2, t1)
    if t1[0] == "D":
        return (t1, t2)
    if t2[0] == "D":
        return (t2, t1)
    return "Error"  


two_throws = set()
for t1, t2 in product(single_throws, single_throws):
    two_throws.add(sort_two_throws(t1, t2))
for t in single_throws:
    two_throws.add(("0", t))
two_throws.add(("0", "0"))

two_throws = list(two_throws)

three_throws = []
for t3 in [s for s in single_throws if s[0] == "D"]:
    for t in two_throws:
        three_throws.append((t[0], t[1], t3))

no_checkouts = 0
for t in three_throws:
    if checkout_value(t) < 100:
        no_checkouts += 1


end = time()
print("Time: " + str(end - start) + " seconds")
print("number of checkouts: " + str(no_checkouts))