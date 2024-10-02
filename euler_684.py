from time import time
import sys
from functools import cache

sys.set_int_max_str_digits(100000)

# Smallest integer with digit sum (m + 9k) is m999...99 (k 9's, 0 <= m < 9).
#
# Given n = m + 9k, then m = n mod 9, and k = n div 9.

def single(n: int) -> int:
    m, k = n % 9, n // 9
    return ((m+1)*10**k - 1) % 1000000007

@cache
def sum_of_singles(n: int) -> int:
    if n == 1:
        return 1
    return (single(n) + sum_of_singles(n - 1)) % 1000000007

start = time()

thesum = 0
a = 1
b = 1
for i in range(2, 91):
    a, b = b, a + b
    
    
print(single(10))
print(sum_of_singles(b))

end = time()
print("Sum: " + str(thesum))
print("Time: " + str(end - start) + " seconds")