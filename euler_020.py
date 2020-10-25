from time import time
from math import factorial

start = time()

s = sum([int(d) for d in str(factorial(100))])

print("Sum of digits: " + str(s))


stop = time()
print("Time: " + str(stop-start))