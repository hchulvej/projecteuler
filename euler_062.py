from time import time

def ordered_string(n):
    return "".join(sorted([c for c in str(n)]))

start = time()

d = {n:ordered_string(n**3) for n in range(100,10000)}

perms = list(d.values())

c = {p:perms.count(p) for p in perms}

candidates = [x for x in c if c[x] == 5]

for i in range(len(candidates)):
    print([n for n in d if d[n] == candidates[i]], min([n for n in d if d[n] == candidates[i]])**3)

stop = time()
print("Time: " + str(stop - start))