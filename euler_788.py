from time import time
from math import floor, comb

binomials = dict()

def binomial(n, k):
    if n == k or k == 0:
        return 1
    if k > n:
        return 0
    if k > n // 2:
        return binomial(n, n - k)
    if (n, k) in binomials:
        return binomials[(n, k)]
    else:
        res = n * binomial(n - 1, k - 1) // k
        binomials[(n, k)] = res
        return res


def dominant1(nd, dd):
    #nd = number of digits
    #dd = dominant digit
    #x = number of instances of the dominant digit
    #y = number of instances of the non-dominant digit
    if dd > 9:
        return 0
    if nd == 1:
        return 1 if dd > 0 else 0
    
    if dd == 0:
        res = 0
        for x in range(floor(nd / 2) + 1, nd + 1):
            y = nd - x
            res += (9 * binomial(nd - 1, x) * pow(9,(y - 1), 1000000007000)) % 1000000007000
        return int(res) % 1000000007000
    else:
        res = 0
        for x in range(floor(nd / 2) + 1, nd + 1):
            y = nd - x
            res += (binomial(nd - 1, x - 1) * pow(9,y, 1000000007000)) % 1000000007000
            res += (8 * binomial(nd - 1, x) * pow(9,(y - 1), 1000000007000)) % 1000000007000
        return int(res) % 1000000007000
        

def dominant2(nd):
    res = 0
    for dd in range(10):
        res += dominant1(nd, dd)
    return res % 1000000007000

def dominant(n):
    res = 0
    for nd in range(1, n + 1):
        res += dominant2(nd) % 1000000007000
    return res

start = time()

print(dominant(2022) % 1000000007)

end = time()
print("Time: " + str(end - start) + " seconds")