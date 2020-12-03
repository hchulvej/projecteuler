from time import time
from itertools import permutations
from math import sqrt

def is_square(n):
    sq = int(sqrt(n))
    return n == sq * sq

with open("p098_words.txt", "r") as f:
    raw = f.readlines()

raw = raw[0].replace("\"", "")
words = raw.split(",")

def are_anagrams(w1, w2):
    if len(w1) != len(w2):
        return False
    return sorted([c for c in w1]) == sorted([c for c in w2])

def check_word_pair(pair):
    w1 = pair[0]
    w2 = pair[1]
    letters = list(set(c for c in w1))
    l = len(letters)

    squares = set()

    for perm in permutations([str(n) for n in range(10)], l):
        nw1 = w1
        nw2 = w2
        for i in range(l):
            nw1 = nw1.replace(letters[i], perm[i])
            nw2 = nw2.replace(letters[i], perm[i])
        if nw1[0] != "0" and nw2[0] != "0":
            if is_square(int(nw1)) and is_square(int(nw2)):
                squares.add(int(nw1))
                squares.add(int(nw2))

    return squares

start = time()

word_pairs = []
for i in range(len(words) - 1):
    for j in range(i + 1, len(words)):
        if are_anagrams(words[i], words[j]):
            word_pairs.append((words[i], words[j]))

largest_square = 0

for pair in word_pairs:
    sqrs = check_word_pair(pair)
    if len(sqrs) > 0:
        m = max(sqrs)
        if m > largest_square:
            largest_square = m

print("Largest square found is: ", largest_square)

stop = time()
print("Time: " + str(stop - start))