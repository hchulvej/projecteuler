from time import time

def db(dec):
    return int(bin(dec)[2:])

def is_palindromic(d):
    return str(d) == str(d)[::-1]

def is_double_palindromic(d):
    return is_palindromic(d) and is_palindromic(db(d))

start = time()

dbpal = 0
for i in range(10**6):
    if is_double_palindromic(i):
        dbpal += i

print("Sum of double palindromes: " + str(dbpal))

stop = time()
print("Time: " + str(stop-start))