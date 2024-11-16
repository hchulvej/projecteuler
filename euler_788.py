from time import time
from math import floor, comb

def dominant1(nd, dd):
    #nd = number of digits
    #dd = dominant digit
    if dd > 9:
        return 0
    if nd == 1:
        return 1 if dd > 0 else 0
    
    if dd == 0:
        # no_dd = number of instances of the dominant digit
        res = 0
        for no_dd in range(floor(nd / 2) + 1, nd + 1):
            no_ndd = nd - no_dd
            res += (9 * comb(nd - 1, no_dd) * pow(9,(no_ndd - 1), 1000000007000)) % 1000000007000
        return int(res) % 1000000007000
    else:
        # no_dd = number of instances of the dominant digit
        res = 0
        for no_dd in range(floor(nd / 2) + 1, nd + 1):
            no_ndd = nd - no_dd
            res += (comb(nd - 1, no_dd - 1) * pow(9,no_ndd, 1000000007000)) % 1000000007000
            res += (8 * comb(nd - 1, no_dd) * pow(9,(no_ndd - 1), 1000000007000)) % 1000000007000
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

print("Too slow")

end = time()
print("Time: " + str(end - start) + " seconds")