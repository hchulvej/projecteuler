from time import time
from sympy import factorint, sieve
from itertools import product

F_120 = 5358359254990966640871840 #= 2^5 * 3^2 * 5 * 7 * 11 * 23 * 31 * 41 * 61 * 241 * 2161 * 2521 * 20641
F_121 = 8670007398507948658051921 #= 89 * 97415813466381445596089



def basic_pisano(n: int) -> int:
    if n < 2:
        return 1
    else:
        a, b = 1, 1
        i = 1
        while a != 0 or b != 1:
            a, b = b, (a + b) % n
            i += 1
        return i

start = time()
sum = 0

coeffs = product(range(6), range(3), range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2))
candidates = []

for c in coeffs:
    n = (2**c[0])*(3**c[1])*(5**c[2])*(7**c[3])*(11**c[4])*(23**c[5])*(31**c[6])*(41**c[7])*(61**c[8])*(241**c[9])*(2161**c[10])*(2521**c[11])*(20641**c[12])
    if n < 1000000000:
        candidates.append(n)
    
for n in candidates:
    if basic_pisano(n) == 120:
        sum += n

end = time()
print("Sum: " + str(sum))
print("Time: " + str(end - start) + " seconds")