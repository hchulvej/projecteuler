from time import time

start = time()

sum_of_proper = [0] + [1] * 10 ** 6

for n in range(2, 5 * 10 ** 5 + 1):
    k = 2 * n
    while k < 10 ** 6 + 1:
        sum_of_proper[k] += n
        k += n

chains = {n:[n] for n in range(1, 10 ** 6 + 1)}
checked = [True, True] + [False] * (10 ** 6 - 1)

for n in range(2, 10 ** 6 + 1):

    if not checked[n]:
        chain = [n]

        m = sum_of_proper[n]

        if m != n and m <= 10 ** 6:
            chain.append(m)

        searching = True

        while searching:
            if m > 10 ** 6:
                searching = False
            else:
                m = sum_of_proper[m]

                if m in chain or m > 10 ** 6:
                    searching = False
                else:
                    chain.append(m)

        if m < 10 ** 6 + 1:
            k = chain.index(m)

            chain = chain[k:]

            for t in chain:
                chains[t] = chain
                checked[t] = True

chain_lengths = {n:len(chains[n]) for n in range(1, 10 ** 6 + 1)}

mc = max(chain_lengths.values())
smallest = min([n for n in range(1, 10 ** 6 + 1) if chain_lengths[n] == mc])

print("Smallest number and chain length: ", smallest, mc)

stop = time()
print("Time: " + str(stop - start))