import sys

coords = []
for line in sys.stdin:
    coords.append([int(z) for z in line.strip().split(',')])

best = 0
for i, c1 in enumerate(coords):
    for c2 in coords[i+1:]:
        best = max(best, (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1))

print(best)