from time import time

def is_palindromic(s):
    return s == s[::-1]

def iteration(s):
    return str(int(s) + int(s[::-1]))

def is_lychrel(n):
    s = str(n)
    step = 1
    it = iteration(s)
    lychrel = not is_palindromic(it)
    while step < 50:
        it = iteration(it)
        if is_palindromic(it):
            lychrel = False
        step += 1
    return lychrel

start = time()

print("Number of Lychrel numbers: " + str(len(set(n for n in range(10000) if is_lychrel(n)))))

stop = time()
print("Time: " + str(stop-start))