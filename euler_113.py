from math import comb
## Number of increasing numbers with N digits is C(N+8,8)
## Number of descreasing numbers with N digits is C(N+9,9) - 1
## Numbers with only one repeating digit are counted twice, so we subtract 9 each time
def non_bouncy(N: int) -> int:
    return comb(N + 8, 8) + comb(N + 9, 9) - 10

def non_bouncy_below(N: int) -> int:
    res = 0
    for n in range(1, N + 1):
        res += non_bouncy(n)
    return res

print(non_bouncy_below(100))