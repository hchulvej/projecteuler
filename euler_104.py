from time import time
from eulerlib import is_pandigital
from math import log10, sqrt

start = time()

fibo = [1, 1]
k = 2

log_golden = log10((1 + sqrt(5)) / 2)
log_root = log10(5) / 2


found = False

while not found:
    fibo = [fibo[1] % 10 ** 9, (fibo[0] + fibo[1]) % 10 ** 9]
    k += 1

    if is_pandigital(fibo[1], 1, 9):
        t = k * log_golden - log_root
        f = int(pow(10, t - int(t) + 8))
        if is_pandigital(f, 1, 9):
           found = True

print("Value: ", k)



stop = time()
print("Time: " + str(stop - start))