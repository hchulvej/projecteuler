from time import time

alphabet = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ"
raw_data = []

def score(word):
    return sum([alphabet.index(w) for w in word])

start = time()

with open("p022_names.txt","r") as f:
    raw_data = f.readlines()

raw_data = raw_data[0].replace('"','')
data = sorted(raw_data.split(","))

print("Total score: " + str(sum([score(word)*(data.index(word) + 1) for word in data])))


stop = time()
print("Time: " + str(stop-start))