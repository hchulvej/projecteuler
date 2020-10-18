from time import time
from primePy import primes
from itertools import chain, combinations, combinations_with_replacement
from numpy import prod

def powerset(it):
    s = list(it)
    return chain.from_iterable(combinations(s,r) for r in range(len(s) + 1))


def proper_factors(n):
    prime_factors = primes.factors(n)
    pow_set = powerset(prime_factors)
    prop_facts = set()
    for ps in pow_set:
        p = int(prod(ps))
        if p < n:
            prop_facts.add(p)
    return prop_facts


start = time()

abundant = [n for n in range(2,28124) if sum(proper_factors(n)) > n]

sum_abundant = set([mn[0] + mn[1] for mn in combinations_with_replacement(abundant,2)])

not_a_sum = [n for n in range(28124) if n not in sum_abundant]

print("Sum of numbers that are not a sum of two abundant numbers: " + str(sum(not_a_sum)))

stop = time()
print("Time: " + str(stop-start))