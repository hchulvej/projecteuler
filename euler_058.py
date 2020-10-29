from time import time
from math import sqrt
from primesieve import Iterator

def is_prime(n):
    it = Iterator()
    p = it.next_prime()

    lim = int(sqrt(n)) + 1
    while p < lim:
        if n%p == 0:
            return False
        p = it.next_prime()
    return True

start = time()

prime_diagonals = []
ratio = 1
l = 3

while ratio > 0.1:
    for k in range(1,4):
        if is_prime(l**2 - k * (l - 1)):
            prime_diagonals.append(l**2 - k * (l - 1))
    ratio = len(prime_diagonals) / (2 * l - 1)
    if ratio < 0.1:
        print("Side length and ratio: " + str((l,ratio)))
    l += 2


stop = time()
print("Time: " + str(stop-start))