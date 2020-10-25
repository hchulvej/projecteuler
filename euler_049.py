from time import time
from primePy import primes

def are_perms(p,q):
    return sorted(str(p)) == sorted(str(q))

start = time()

p_list = list(primes.between(1000,10000))


for p in p_list:
    for q in p_list:
        if p < q:
            if q + (q - p) in p_list:
                if are_perms(p,q) and are_perms(p, 2 * q - p):
                    print((p, q, 2 * q - p), str(p) + str(q) + str(2 * q - p))





stop = time()
print("Time: " + str(stop-start))