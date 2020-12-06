from time import time
from math import gcd

def minmax_digit(n):
    digits = set(int(d) for d in str(n))
    return (min(digits), max(digits))

def is_bouncy(n):
    if n < 100:
        return False
    up, down = False, False
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1):
        if digits[i] < digits[i + 1]:
            up = True
        if digits[i] > digits[i + 1]:
            down = True
    return up and down

start = time()

bouncy = 1
n = 101

while bouncy / n < 0.99:
    n += 1
    if is_bouncy(n):
        bouncy += 1

print(bouncy, n, bouncy / n)


stop = time()

print("Time: ", stop - start)