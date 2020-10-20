from time import time
from math import gcd
from numpy import prod

def check_fraction(frac):
    num = frac[0]
    den = frac[1]
    n = sorted(str(num))
    d = sorted(str(den))
    if n[0] == d[0]:
        return num*int(d[1]) == den*int(n[1])
    if n[1] == d[1]:
        return num * int(d[0]) == den * int(n[0])
    return False


start = time()

fractions = set()

for num in [n for n in range(10,100) if n%10 > 0]:
    for den in range(num + 1,100):
        if check_fraction((num,den)):
            fractions.add((num,den))

num_prod = prod([f[0] for f in fractions])
den_prod = prod([f[1] for f in fractions])

print("The denominator is: " + str(den_prod // gcd(num_prod, den_prod)))

stop = time()
print("Time: " + str(stop-start))