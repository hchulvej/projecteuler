from time import time
from gmpy2 import is_prime

start = time()

def is_Harshad(v, s):
    return v % s == 0

# Right Truncattable Harshad numbers
RTH_numbers = dict()
for nd in range(1,14):
    RTH_numbers[nd] = []

for d in range(1,10):
    RTH_numbers[1].append((d,d))   

def add_digit_to_Harshad(nd):
    existing_numbers = RTH_numbers[nd - 1]
    for e in existing_numbers:
        for d in range(0,10):
            if is_Harshad(e[0] * 10 + d, e[1] + d):
                RTH_numbers[nd].append((e[0] * 10 + d, e[1] + d))

for nd in range(2,14):
    add_digit_to_Harshad(nd)

print(len(RTH_numbers[13]))

end = time()
print("Time: " + str(end - start) + " seconds")