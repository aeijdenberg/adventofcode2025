import math
import sys

coords = []
for l in sys.stdin:
    coords.append([int(x) for x in l.strip().split(',')])

dists = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        dists.append((math.sqrt(sum([math.pow(coords[i][k] - coords[j][k], 2) for k in range(3)])), i, j))
dists.sort(key=lambda x: x[0])

circuits = {}
for round in range(len(dists)):
    _, next1, next2 = dists[round]
    c = set()
    for n in [next1, next2]:
        c.add(n)
        for nn in circuits.get(n, set()):
            c.add(nn)
    for n in c:
        circuits[n] = c
    if len(c) == len(coords):
        print(coords[next1][0]*coords[next2][0])
        break
