from math import log10
import itertools

upper_limit = 10**9

# 25 primes
list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
limits_of_ranges = [int(9/log10(p)) for p in list_of_primes]

def satisfying_number(list_of_powers):
    number = 1
    for i, power in enumerate(list_of_powers):
        number *= list_of_primes[i] ** power
    return number <= upper_limit

def count_satisfying_numbers(limits_of_ranges):
    count = 0
    
    # 1. Lav en liste med range-objekter for alle 25 p'ere
    # limits_of_ranges skal nu være en liste med 25 tal
    ranges = [range(0, limit) for limit in limits_of_ranges]
    
    # 2. itertools.product(*ranges) genererer alle kombinationer.
    # '*' pakker listen ud, så det svarer til product(range1, range2, ..., range25)
    for p_combination in itertools.product(*ranges):
        
        # p_combination er en tuple, f.eks. (0, 0, 0, ..., 0)
        # Hvis din funktion kræver en liste, laver vi den hurtigt om med list()
        if satisfying_number(list(p_combination)):
            count += 1
            
    return count

print(count_satisfying_numbers(limits_of_ranges))