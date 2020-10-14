from time import time

def fib():
    prev, curr = 1, 2
    yield prev
    yield curr
    while True:
        [curr, prev] = [prev + curr, curr]
        yield curr

fib_gen = fib()

start = time()

fibonacci = next(fib_gen)
cumulated = 0

while fibonacci < 4000000:
    if fibonacci%2 == 0:
        cumulated += fibonacci
    fibonacci = next(fib_gen)

stop = time()

print("Sum is " + str(cumulated))
print("Time: " + str(stop-start))