from time import time
## (x+2k)^2-(x+k)^2-x^2 = (x+k)(3k-x)
## Assume: k > 0
## 3k-x > 0 <=> x < 3k
## (x+k)(3k-x) < 1000000

## x < 750000

start = time()

scores = []
counter = dict()

for x in range(1, 750000):
    k = int(x/3)
    while (x+k)*(3*k-x) < 1000000:
        if (x+k)*(3*k-x) in counter:
            counter[(x+k)*(3*k-x)] += 1
        else:
            counter[(x+k)*(3*k-x)] = 1
        k += 1

end = time()
       
print(len([n for n in counter if counter[n] == 10]))
print("Time: " + str(end - start) + " seconds")