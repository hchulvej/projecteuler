from time import time
from itertools import combinations_with_replacement

def check(s, p):
    if s[0] in p:
        i = p.index(s[0])
        q = p[i + 1:]
        if s[1] in q:
            j = q.index(s[1])
            r = q[j + 1:]
            if s[2] in r:
                return True
    return  False

def check_all(p):
    for s in suc:
        if not check(s, p):
            return False
    return True

start = time()

suc = set()

with open("p079_keylog.txt", "r") as file:
    for l in file.readlines():
        suc.add(l.replace("\n", ""))


bingo = False
n = 1000

while not bingo:
    if check_all(str(n)):
        print(n)
        bingo = True
        break
    n += 1





stop = time()
print("Time: " + str(stop - start))