from time import time

def next_collatz(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n + 1

def chain_length(n):
    length = 2
    k = next_collatz(n)
    while k > 1:
        length += 1
        k = next_collatz(k)
    return length

start = time()

longest = chain_length(1)
top_dog = 1

for n in range(1,10**6):
    cl = chain_length(n)
    if longest < cl:
        longest = cl
        top_dog = n

print("Longest chain is achieved when n = " + str(top_dog) + " and is " + str(longest))

stop = time()
print("Time: " + str(stop-start))