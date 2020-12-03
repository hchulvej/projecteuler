from time import time
from math import log10

with open("p099_base_exp.txt", "r") as f:
    raw = f.readlines()

powers = []

for i in range(len(raw)):
    p = raw[i].replace("\n", "")
    p = list(map(int, p.split(",")))
    powers.append(p)

start = time()

f = {n:powers[n][1] * log10(powers[n][0]) for n in range(len(powers))}

i = 0
m = f[i]

for j in range(len(powers)):
    if f[j] > m:
        i = j
        m = f[j]


print("Line with largest power: ", i + 1)

stop = time()
print("Time: " + str(stop - start))