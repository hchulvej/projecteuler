from time import time

romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
r2n = dict(zip(romans, numbers))
n2r = dict(zip(numbers, romans))

def integer_to_roman(n):
    d = {r:0 for r in romans}

    rem = n

    for k in numbers[::-1]:
        d[n2r[k]] = rem // k
        rem = rem - k * (rem // k)

    rom = ""

    for r in d.keys():
        if d[r] > 0:
            rom = r * d[r] + rom

    return rom


start = time()

list_of_roman_numerals = []

with open("p089_roman.txt", "r") as f:
    raw = f.readlines()
    for l in raw:
        l = l.replace("\n", "")
        nl = l
        for rep in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            nl = nl.replace(rep, "*" + str(r2n[rep]) + "*")
        nl = nl.split("*")

        val = 0
        for s in nl:
            try:
                if int(s) in [4, 9, 40, 90, 400, 900]:
                    val += int(s)
            except:
                nums = [c for c in s]
                val += sum([r2n[r] for r in nums])

        list_of_roman_numerals.append((l, val))


characters_saved = 0

for l in list_of_roman_numerals:
    characters_saved += len(l[0]) - len(integer_to_roman(l[1]))

print("Characters saved: ", characters_saved)

stop = time()
print("Time: " + str(stop - start))