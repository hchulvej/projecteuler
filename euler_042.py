from time import time


with open("p042_words.txt","r") as f:
    raw = f.readlines()

alphabet = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def score(w):
    return sum([alphabet.index(l) for l in w])

start = time()

raw = raw[0].split(",")
for i in range(len(raw)):
    raw[i] = raw[i].replace("\"","")

scores = [score(w) for w in raw]

lim = max(scores)

triangles = []

n = 1
while n*(n + 1) // 2 < lim + 1:
    triangles.append(n*(n + 1) // 2)
    n += 1

tw = len([s for s in scores if s in triangles])

print("Number of triangle words: " + str(tw))

stop = time()
print("Time: " + str(stop-start))