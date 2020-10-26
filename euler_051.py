from time import time
import primesieve

def blueprints(p):
    bps = set()
    s = str(p)
    for d in s:
        bps.add(s.replace(d, "*"))
    return bps

def bp_to_primes(bp):
    return len(set(int(bp.replace("*", str(k))) for k in range(10) if int(bp.replace("*", str(k))) in prime_list))

start = time()

prime_list = list(primesieve.primes(50000, 10**6))

print("Prime list generated!")

for p in prime_list:
    for bp in blueprints(p):
        if bp_to_primes(bp) == 8:
            print("Smallest prime: " + str(p) + ", blueprint = " + bp)
            break


stop = time()
print("Time: " + str(stop-start))