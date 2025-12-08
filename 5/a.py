import sys

ranges = []
actives = []
for l in sys.stdin:
    l = l.strip()
    if len(l):
        if '-' in l:
            ranges.append([int(x) for x in l.split('-')])
        else:
            actives.append(int(l))

rv = 0
for i in actives:
    fresh = False
    for r in ranges:
        if r[0] <= i and i <= r[1]:
            fresh = True
            break

    if fresh:
        rv += 1

print(rv)
