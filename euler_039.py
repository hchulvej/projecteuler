from time import time
from math import gcd
from collections import Counter

def perim(m,n,k):
    return 2*m*(m+n)*k


start = time()

perims = []

for n in range(1,251):
    for m in [t for t in range(n+1,251,2) if gcd(n,t) == 1]:
        k = 1
        while perim(m,n,k) < 1001:
            perims.append(perim(m,n,k))
            k += 1

c = Counter(perims)

print("The maximising perimeter is: " + str(c.most_common(1)[0][0]))


stop = time()
print("Time: " + str(stop-start))