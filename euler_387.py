from time import time
from gmpy2 import is_prime

start = time()

# Right-truncable Harshad numbers
RTH_numbers = dict()
for nd in range(1,13):
    RTH_numbers[nd] = []

for d in range(1,10):
    RTH_numbers[1].append((d,d))

for n in range(2,13):
    for d in range(10):    
        for h in RTH_numbers[n - 1]:
            if (10*h[0] + d) % (h[1] + d) == 0:
                RTH_numbers[n].append((10*h[0] + d, h[1] + d))

# Strong right-truncable Harshad numbers
RTSH_numbers = dict()
for nd in range(2,13):
    RTSH_numbers[nd] = [h for h in RTH_numbers[nd] if is_prime(h[0] // h[1])]

# Strong right-truncable Harshad primes



end = time()
print("Time: " + str(end - start) + " seconds")