from time import time
from math import sqrt
import functools

memo = {}

def partitions(s):
    if len(s) > 0:
        for i in range(1, len(s)+1):
            first, rest = s[:i], s[i:]
            for p in partitions(rest):
                yield [first] + p
    else:
        yield []

@functools.lru_cache
def is_s_number(N: int) -> bool:
    return int(sqrt(N)) in [sum(list(map(int, p))) for p in partitions(str(N)) if len(p) > 1]

start = time()

print(sum([n**2 for n in range(1, 1000001) if is_s_number(n**2)]))

end = time()

print("Time: ", end - start)