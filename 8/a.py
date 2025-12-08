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
for round in range(1000):
    _, next1, next2 = dists[round]
    in1, in2 = next1 in circuits, next2 in circuits
    c = set()
    for n in [next1, next2]:
        c.add(n)
        for nn in circuits.get(n, set()):
            c.add(nn)
    for n in c:
        circuits[n] = c

uniques = list(set(frozenset(x) for x in circuits.values()))
uniques.sort(key=lambda x: len(x), reverse=True)
rv = 1
for i in range(3):
    rv *= len(uniques[i])
print(rv)