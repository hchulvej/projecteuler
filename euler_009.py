from time import time
from itertools import product


start = time()

for ij in product(range(1,500),repeat=2):
    a = ij[0]
    b = ij[1]
    c = 1000 - a - b
    if a**2 + b**2 == c**2:
        print("(a,b,c) = " + str((a,b,c)) + " - product is " + str(a*b*c))
        break

stop = time()
print("Time: " + str(stop-start))