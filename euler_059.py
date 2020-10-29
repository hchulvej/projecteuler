from time import time
from itertools import product

start = time()

with open("p059_cipher.txt", "r") as f:
    raw = f.read().split(",")

cipher = list(map(int, raw))

for p in product("abcdefghijklmnopqrstuvxyz", repeat=3):
    short_key = p[0] + p[1] + p[2]
    long_key = short_key * 485
    long_key_i = [ord(c) for c in long_key]

    message = [long_key_i[i]^cipher[i] for i in range(len(cipher))]
    message_l = list(map(chr, message))

    if " and " in "".join(message_l):
        print("".join(message_l))
        print(short_key)
        print(sum(message))



stop = time()
print("Time: " + str(stop - start))