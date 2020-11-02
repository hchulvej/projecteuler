from time import time
from math import sqrt, floor

def len_cf_of_square_root(n):
    if sqrt(n) == floor(sqrt(n)):
        return 0
    a = [floor(sqrt(n))]
    b = [0, a[0]]
    c = [0, n - a[0]**2]
    i = 1
    while a[-1] != 2 * a[0]:
        i += 1
        a.append(floor((a[0] + b[i-1]) / c[i-1]))
        b.append(a[i-1] * c[i-1] - b[i-1])
        c.append((n - b[i]**2) / c[i-1])
    return len(a) - 1

start = time()

odd = 0

for n in range(1,10001):
    p = len_cf_of_square_root(n)
    if p%2 == 1:
        odd += 1

print("Number of odd-period CFs: " + str(odd))


stop = time()
print("Time: " + str(stop-start))