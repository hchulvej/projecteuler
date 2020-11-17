from time import time
from random import randint, shuffle
from collections import deque, Counter

def roll():
    die1 = randint(1, 4)
    die2 = randint(1, 4)
    return (die1 + die2, die1 == die2)

def chance():
    text = ["Nothing"] * 6 + ["Go", "Jail", "C1", "E3", "H2", "R1", "Next R", "Next R", "Next U", "Back 3"]
    shuffle(text)
    return deque(text)

def community_chest():
    text = ["Nothing"] * 14 + ["Go", "Jail"]
    shuffle(text)
    return deque(text)

def process_text(text, pos):
    if text == "Nothing":
        return pos
    if text == "Go":
        return 0
    if text == "Jail":
        return 10
    if text == "C1":
        return 11
    if text == "E3":
        return 24
    if text == "H2":
        return 39
    if text == "R1":
        return 5
    if text == "Next R":
        if pos in [2, 36]:
            return 5
        if pos == 7:
            return 15
        if pos in [17, 22]:
            return 25
        if pos == 33:
            return 35
    if text == "Next U":
        if pos in [17, 22]:
            return 28
        else:
            return 12
    if text == "Back 3":
        return (pos + 40  - 3)%40

start = time()

#Setup decks
cc1 = community_chest()
cc2 = community_chest()
cc3 = community_chest()
ch1 = chance()
ch2 = chance()
ch3 = chance()

#Starting the simulation
pos = 0
visited = Counter()
last_two_rolls = []

#The simulation
for it in range(100000):

    new_roll = roll()

    new_pos = (pos + new_roll[0])%40

    if new_pos == 30:
        new_pos = 10

    if new_pos == 2:
        text = cc1.popleft()
        cc1.append(text)
        new_pos = process_text(text, new_pos)

    if new_pos == 17:
        text = cc2.popleft()
        cc2.append(text)
        new_pos = process_text(text, new_pos)

    if new_pos == 33:
        text = cc3.popleft()
        cc3.append(text)
        new_pos = process_text(text, new_pos)

    if new_pos == 7:
        text = ch1.popleft()
        ch1.append(text)
        new_pos = process_text(text, new_pos)

    if new_pos == 22:
        text = ch2.popleft()
        ch2.append(text)
        new_pos = process_text(text, new_pos)

    if new_pos == 36:
        text = ch3.popleft()
        ch3.append(text)
        new_pos = process_text(text, new_pos)

    #Checking for double rolls
    last_two_rolls = [new_roll[1]] + last_two_rolls
    if len(last_two_rolls) == 3 and all(last_two_rolls):
        new_pos = 10

    visited.update([new_pos])

    pos = new_pos

print(visited.most_common(5))

stop = time()
print("Time: " + str(stop-start))