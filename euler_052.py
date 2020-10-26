from time import time
from itertools import count

def limit(n):
    return int("9"*n) // 6

def solve():
    for n in count(1):
        for x in range(10**(n - 1),limit(n)):
            found = True
            for k in range(1, 6):
                if "".join(sorted(str(k*x))) != "".join(sorted(str((k + 1)*x))):
                    found = False
            if found:
                return x


start = time()

print(solve())

stop = time()
print("Time: " + str(stop-start))