from time import time
from itertools import product

def total(two,five,ten,twenty,fifty,quid,twoquid):
    return 2*two + 5*five + 10*ten + 20*twenty + 50*fifty + 100*quid + 200*twoquid

start = time()

ways = 0

two_p = [n for n in range(101)]
five_p = [n for n in range(41)]
ten_p = [n for n in range(21)]
twenty_p = [n for n in range(11)]
fifty_p = [n for n in range(5)]
one_q = [n for n in range(3)]
two_q = [n for n in range(2)]

for comb in product(two_p,five_p,ten_p,twenty_p,fifty_p,one_q,two_q):
    ones = 200 - total(comb[0],comb[1],comb[2],comb[3],comb[4],comb[5],comb[6])
    if ones >= 0:
        ways += 1

print("Number of ways: " + str(ways))


stop = time()
print("Time: " + str(stop-start))