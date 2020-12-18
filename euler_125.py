from time import time
from eulerlib import is_palindrome

def sum_of_squares(s, n):
    return int((6*s*s*n + 6*n*(n-1)*s + n*(2*n-1)*(n-1))/6)

start = time()

total = 0

counted = set()

for s in range(1, 7071):
    for n in range(2, 669):
        sq = sum_of_squares(s, n)
        if sq < 10**8 and is_palindrome(sq, 10) and not sq in counted:
            total += sq
            counted.add(sq)


print("Total sum is:", total)



stop = time()
print("Time: " + str(stop - start))