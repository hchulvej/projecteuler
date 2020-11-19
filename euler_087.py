from time import time
from primePy import primes
from itertools import product

def power(x, y, z):
    return x ** 2 + y ** 3 + z ** 4

start = time()

numbers = set()


p_list_one = primes.upto(7071)
p_list_two = primes.upto(367)
p_list_three = primes.upto(83)

for t in product(p_list_one, p_list_two, p_list_three):
    p = power(t[0], t[1], t[2])
    if p < 50000000:
        numbers.add(p)




print("Number of prime power triples: ", len(numbers))

stop = time()
print("Time: " + str(stop - start))