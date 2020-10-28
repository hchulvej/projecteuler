from time import time

def create_hands():
    player1 = []
    player2 = []
    with open("p054_poker.txt", "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.split(" ")
            player1.append(line[:5])
            player2.append(line[5:])
    return (player1, player2)

def value(c):
    if c[0] in ["T", "J", "Q", "K", "A"]:
        return ["T", "J", "Q", "K", "A"].index(c[0]) + 10
    return int(c[0])

def values(h):
    return [value(c) for c in h]

def suits(h):
    return [c[1] for c in h]

def evaluate_hand(h):
    v = values(h)
    cts = [v.count(val) for val in v]
    s = suits(h)
    scores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    highest = sorted(v, reverse=True)

    #One pair.
    if sorted(cts) == [1, 1, 1, 2, 2]:
        for val in v:
            if v.count(val) == 2:
                scores[8] = val
    else:
        scores[8] = 0

    #Two pairs.
    if sorted(cts) == [1, 2, 2, 2, 2]:
        m = 0
        for val in v:
            if v.count(val) == 2 and val > m:
                m = val
        scores[7] = m
    else:
        scores[7] = 0

    #Three of a kind.
    if sorted(cts) == [1, 1, 3, 3, 3]:
        for val in v:
            if v.count(val) == 3:
                scores[6] = val
    else:
        scores[6] = 0

    #Straight.
    if sorted(cts) == [1, 1, 1, 1, 1] and max(v)%14 - min(v) == 4:
        scores[5] = max(v)
    else:
        scores[5] = 0

    #Flush. Also includes Straight Flush and Royal Flush.
    if len(s) == 1:
        scores[4] = 1
    else:
        scores[4] = 0

    #Full House.
    if sorted(cts) == [2, 2, 3, 3, 3]:
        m = 0
        for val in v:
            if v.count(val) == 3:
                m = val
        scores[3] = m
    else:
        scores[3] = 0

    #Four of a kind.
    if sorted(cts) == [1, 4, 4, 4, 4]:
        m = 0
        for val in v:
            if v.count(val) == 4:
                m = val
        scores[2] = m
    else:
        scores[2] = 0

    #Straight Flush.
    if sorted(cts) == [1, 1, 1, 1, 1] and max(v)%14 - min(v) == 4 and len(s) == 1:
        scores[1] = max(v)
    else:
        scores[1] = 0

    #Royal Flush.
    if sorted(cts) == [1, 1, 1, 1, 1] and max(v) == 14 and len(s) == 1:
        scores[0] = 1
    else:
        scores[0] = 0

    return (scores, highest)

def compare_hands(h1, h2):
    e1 = evaluate_hand(h1)
    e2 = evaluate_hand(h2)
    winner = 0
    for i in range(9):
        if e1[0][i] == e2[0][i]:
            continue
        else:
            if e1[0][i] > e2[0][i]:
                winner = 1
            else:
                winner = 2
            break

    if winner != 0:
        return winner
    else:
        for i in range(5):
            if e1[1][i] == e2[1][i]:
                continue
            else:
                if e1[1][i] > e2[1][i]:
                    winner = 1
                else:
                    winner = 2
                break

    return winner


start = time()

p = create_hands()
p1, p2 = p[0], p[1]

p1_wins = 0
for i in range(len(p1)):
    if compare_hands(p1[i], p2[i]) == 1:
        p1_wins += 1

print("Player 1 wins " + str(p1_wins) + " hands")

stop = time()
print("Time: " + str(stop-start))