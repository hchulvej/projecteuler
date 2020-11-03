from time import time
from itertools import permutations


def check_5_gon(f):
    s_one = f[0] + f[1] + f[3]
    if f[2] + f[3] + f[5] != s_one:
        return False
    if f[7] + f[5] + f[4] != s_one:
        return False
    if f[8] + f[7] + f[6] != s_one:
        return False
    if f[9] + f[8] + f[1] != s_one:
        return False
    return True

def to_string_5_gon(f):
    min_index = f.index(min(f[0], f[2], f[4], f[6], f[9]))
    s = list(map(str,list(f)))
    if min_index == 0:
        return s[0] + s[1] + s[3] + s[2] + s[3] + s[5] + s[4] + s[5] + s[7] + s[6] + s[7] + s[8] + s[9] + s[8] + s[1]
    if min_index == 2:
        return s[2] + s[3] + s[5] + s[4] + s[5] + s[7] + s[6] + s[7] + s[8] + s[9] + s[8] + s[1] + s[0] + s[1] + s[3]
    if min_index == 4:
        return s[4] + s[5] + s[7] + s[6] + s[7] + s[8] + s[9] + s[8] + s[1] + s[0] + s[1] + s[3] + s[2] + s[3] + s[5]
    if min_index == 6:
        return s[6] + s[7] + s[8] + s[9] + s[8] + s[1] + s[0] + s[1] + s[3] + s[2] + s[3] + s[5] + s[4] + s[5] + s[7]
    if min_index == 9:
        return s[9] + s[8] + s[1] + s[0] + s[1] + s[3] + s[2] + s[3] + s[5] + s[4] + s[5] + s[7] + s[6] + s[7] + s[8]


start = time()

valid = set()

for p in permutations([1,2,3,4,5,6,7,8,9,10]):
    if check_5_gon(p):
        valid.add(p)

strings = set()

for v in valid:
    s = to_string_5_gon(v)
    if len(s) == 16:
        strings.add(int(s))

print("Maximal string: " + str(max(strings)))

stop = time()
print("Time: " + str(stop - start))