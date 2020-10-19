from time import time
from primePy import primes

def consec(a,b):
    n = 0
    while n*(n+a)+b > 0 and primes.check(n*(n+a)+b):
        n += 1
    return n

start = time()

b_vals = list(primes.upto(1000))

max_primes = 0
max_a_b_ab = (0,0,0)

for b in b_vals:
    for a in range(1-b,b):
        c = consec(a,b)
        if c > max_primes:
            [max_primes, max_a_b_ab] = [c, (a,b,a*b)]

print(max_a_b_ab)

stop = time()
print("Time: " + str(stop-start))