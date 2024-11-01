from time import time
from gmpy2 import next_prime, mpz

start = time()
## Notation
#
# a(n) = min({ k | F_k mod n = 0 })
#
# pi(n): period length of {F_k mod n, k = 0, 1, 2, ...}
#
# L_n = F_(n-1) + F_(n+1)
#
# Vinson's theorem:
#
# For n >= 2:
# a(n) odd: pi(n) = 4*a(n)
# a(n) even:
#   n mod 8 <> 0 AND a(p) mod 4 = 2 for all p>2 prime factors in n: pi(n) = a(n)
#   pi(n) = 2*a(n)
#
# In conclusion: pi(n) in {a(n), 2a(n), 4(a(n))}
#
# So, if a(n) > 120, then pi(n) <> 120

F = [0, 1]
L = [2, 1]
i = 1
while L[i] < 10**9:
    F.append(F[i-1] + F[i-2])
    L.append(L[i-1] + L[i-2])
    i += 1

a = dict()
for n in range(2, 38516678):
    for i in range(2, len(F)):
       if F[i] % n == 0:
            if n not in a:
                a[n] = i
                break
            

# If n > 2 and L_t <= n, then pi(n) >= 2t
# L_60 = 29075380
# L_61 = 38516678
# I.e. if n >= 38516678, then pi(n) >= 122
# We limit n to be < 38516678



end = time()
print("Time: " + str(end - start) + " seconds")