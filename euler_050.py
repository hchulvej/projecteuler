from time import time
import primesieve

start = time()

p_list = primesieve.primes(10**6)
cum_sums = {2:2}
for i in range(1,len(p_list)):
    if p_list[i] + cum_sums[p_list[i - 1]] > 10**6:
        break
    else:
        cum_sums[p_list[i]] = p_list[i] + cum_sums[p_list[i - 1]]

max_index = p_list.index(max(cum_sums.keys()))
found = []


m = max_index
while not found:
    for k in range(1, m):
        if cum_sums[p_list[m]] - cum_sums[p_list[k]] in p_list:
            found.append(((cum_sums[p_list[m]] - cum_sums[p_list[k]]), m))
            break
    m -= 1


print("The prime is: " + str(found[0][0]))


stop = time()
print("Time: " + str(stop-start))