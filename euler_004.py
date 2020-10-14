from time import time
from itertools import product

def is_palindrome(num):
    return str(num) == str(num)[::-1]

start = time()

m = max([d[0]*d[1] for d in product(range(100,1000),repeat=2) if is_palindrome(d[0]*d[1])])
print("Largest palindrome: " + str(m))

stop = time()
print("Time: " + str(stop-start))