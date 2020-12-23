from time import time
from primesieve import primes



start = time()

p_list = list(primes(5, 10 ** 6 + 100))
d_list = {p : len(str(p)) for p in p_list}

sum_of_numbers = 0

# 10^d(p1)*x + p1 = 0 (mod p2)
# x = -p1 * (10^d(p1))^(-1) (mod p2)

for i in range(len(p_list) - 1):
    p1, p2 = p_list[i], p_list[i + 1]
    inv = pow(10 ** d_list[p1], -1, p2)
    x = ((-1) * p1 * inv) % p2
    if p1 <= 1000000:
        sum_of_numbers += 10 ** d_list[p1] * x + p1


print("Sum of numbers:", sum_of_numbers)



stop = time()
print("Time: " + str(stop - start))