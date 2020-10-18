from time import time
import calendar

start = time()

sundays = 0

for y in range(1901,2001):
    for m in range(1,13):
        if calendar.weekday(y, m, 1) == 6:
            sundays += 1


print("Number of Sundays: " + str(sundays))


stop = time()
print("Time: " + str(stop-start))

