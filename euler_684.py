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


start = time()

thesum = 0

    
print(sum([single(n) for n in range(18)]))

end = time()
print("Sum: " + str(thesum))
print("Time: " + str(end - start) + " seconds")