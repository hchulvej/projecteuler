from math import gcd
from time import time

start = time()

num = 1
for k in range(2,21):
    num *= k//gcd(num,k)

print("Number is: " + str(num))

stop = time()
print("Time: " + str(stop-start))