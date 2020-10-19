from time import time
from itertools import permutations

start = time()

p = list(permutations([0,1,2,3,4,5,6,7,8,9],10))

n = "".join(map(str,p[999999]))

print("The 10^6th permutation: " + n)

stop = time()
print("Time: " + str(stop-start))