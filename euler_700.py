from time import time

start = time()

eulercoins = [1504170715041707]
smallest_eulercoin = 1504170715041707

tested_numbers = set({1504170715041707})

def sequence():
    n = 1
    while True:
        yield (1504170715041707 * n) % 4503599627370517
        n += 1
        
gen = sequence()

running = True

e_n = next(gen)

while running:
    e_n = next(gen)
    if e_n in tested_numbers:
        running = False
    if e_n < smallest_eulercoin:
        smallest_eulercoin = e_n
        eulercoins.append(e_n)

sum_of_eulercoins = sum(eulercoins)

## NOT DONE - TOO INEFFICIENT

end = time()
print("The sum of all Eulercoins is ", sum_of_eulercoins)
print("Time: " + str(end - start) + " seconds")