from time import time
from math import ceil

def is_pandigital(s):
    return "".join(sorted(s)) == "123456789"

def concat(st_num, n):
    res = ""
    for k in range(1, n + 1):
        res += str(st_num * k)
    return res

start = time()

c = set()

for n in range(2,10):
    for st in range(1, 10**ceil(9/n)):
        con = concat(st, n)
        if len(con) != 9:
            continue
        else:
            if is_pandigital(con):
                c.add((int(con), st, n))

print("Largest pandigital number: " + str(max([e[0] for e in c])))


stop = time()
print("Time: " + str(stop-start))